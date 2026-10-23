import os
import hashlib
import json

MONITOR_DIR = "./monitor_folder"
BASELINE_FILE = "baseline.json"

def calculate_sha256(filepath):
    """Calculate SHA-256 hash fingerprint of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def create_sample_files():
    """Setup target directory and sample file."""
    if not os.path.exists(MONITOR_DIR):
        os.makedirs(MONITOR_DIR)
        print(f"[+] Target folder created: {MONITOR_DIR}")
    
    sample_file = os.path.join(MONITOR_DIR, "system_config.txt")
    if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("SERVER_PORT=8080\nALLOW_ROOT_LOGIN=FALSE\nENABLE_FIREWALL=TRUE\n")
        print(f"[+] Sample file created: {sample_file}")

def create_baseline():
    """Generate SHA-256 baseline signatures."""
    baseline = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_sha256(filepath)
            if file_hash:
                baseline[filepath] = file_hash
    
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    print(f"[+] Baseline successfully generated in '{BASELINE_FILE}'.")

def audit_integrity():
    """Check for file tampering, deletion, or new unauthorized files."""
    if not os.path.exists(BASELINE_FILE):
        print("[!] Error: Baseline file missing. Run Option 1 first!")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_state = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_sha256(filepath)
            if file_hash:
                current_state[filepath] = file_hash

    print("\n==================================================")
    print("      FILE INTEGRITY MONITORING AUDIT REPORT       ")
    print("==================================================")
    
    tampered = False
    for filepath, old_hash in baseline.items():
        if filepath not in current_state:
            print(f"🚨 DELETED FILE: {filepath}")
            tampered = True
        elif current_state[filepath] != old_hash:
            print(f"⚠️  TAMPERED / MODIFIED FILE: {filepath}")
            print(f"    - Baseline Hash: {old_hash[:16]}...")
            print(f"    - Current  Hash: {current_state[filepath][:16]}...")
            tampered = True

    for filepath in current_state:
        if filepath not in baseline:
            print(f"⚠️  NEW UNTRUSTED FILE DETECTED: {filepath}")
            tampered = True

    if not tampered:
        print("✅ INTEGRITY INTACT: All files match baseline signatures!")

def main():
    create_sample_files()
    while True:
        print("\n--- File Integrity Monitor ---")
        print("1. Generate Baseline (Take Fingerprint)")
        print("2. Run Integrity Audit Check")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == '1':
            create_baseline()
        elif choice == '2':
            audit_integrity()
        elif choice == '3':
            print("Exiting Monitor.")
            break

if __name__ == "__main__":
    main()
