# File Integrity Monitor (FIM) 🛡️

A lightweight, robust host-based Security Monitoring system written in Python. This tool uses **SHA-256 cryptographic hashing** to generate digital signatures (fingerprints) for critical system files and detects unauthorized edits, file deletions, or new untrusted file additions in real-time.

---

## 📌 Project Overview
In modern security infrastructure, attackers and malware often attempt to compromise systems by modifying core configuration files, modifying source code, or dropping unauthorized executable scripts. 

**File Integrity Monitor (FIM)** solves this by maintaining a trusted baseline database (`baseline.json`) containing cryptographic SHA-256 hashes of all monitored files. During audit checks, it re-calculates hashes in 4KB chunks and alerts administrators immediately if any signature mismatch is discovered.

---

## 🚀 Key Features
- **SHA-256 Cryptographic Hashing:** Computes secure 256-bit hash signatures for exact file state verification.
- **Baseline Snapshot Management:** Generates and exports known-good hashes to structured JSON files (`baseline.json`).
- **Comprehensive Tamper Detection:**
  - ⚠️ **Modified Files:** Flags content edits, configuration changes, or payload injections.
  - 🚨 **Deleted Files:** Detects missing critical system files.
  - ⚠️ **New Untrusted Files:** Highlights unknown or newly dropped files.
- **Zero Third-Party Dependencies:** Built entirely with Python standard libraries (`hashlib`, `os`, `json`) for 100% cross-platform compatibility (Windows, macOS, Linux, PyDroid).

---

## 📂 Project Directory Structure

```text
file_integrity_monitor/
├── file_integrity_monitor.py   # Main Python Application Logic
├── baseline.json               # Auto-generated Cryptographic Baseline (DO NOT EDIT MANUALLY)
├── requirements.txt            # Dependency configuration file
├── README.md                   # Project Documentation
└── monitor_folder/             # Target directory containing monitored files
    └── system_config.txt       # Sample monitored configuration file
```

---

## 🛠️ Requirements & Setup

Since this tool uses standard Python modules, **no external library installation is needed**!

- **Python Version:** Python 3.8+

---

## 💻 How to Run & Test

### Step 1: Launch the Program
Open terminal or command prompt in your project directory and execute:
```bash
python file_integrity_monitor.py
```

### Step 2: Generate Initial Baseline
1. From the menu, select option **`1`** (`Generate New Baseline`).
2. The script scans all files inside `./monitor_folder` and creates `baseline.json`.

### Step 3: Run Integrity Audit
Select option **`2`** (`Run Integrity Audit Check`).
- **Initial Result:** `✅ INTEGRITY INTACT: All monitored files match the baseline signature!`

### Step 4: Simulate Cyber Attack / File Tampering
1. Open `monitor_folder/system_config.txt` in a text editor.
2. Edit any character, add a new line, or delete a word, then save.
3. Return to the script and run option **`2`** (`Run Integrity Audit Check`).
- **Expected Alert:** 
  ```text
  ⚠️ TAMPERED/MODIFIED FILE DETECTED: ./monitor_folder/system_config.txt
      - Original SHA-256: e3b0c44298fc1c14...
      - Current  SHA-256: 8d969eef6ecad3c2...
  ```

---

## 🛡️ Security Use Cases
- **Host Intrusion Detection Systems (HIDS):** Auditing `/etc/passwd` or system configuration files.
- **Malware Forensics:** Spotting unauthorized ransomware or Trojan file overrides.
- **Compliance Standards:** Fulfilling PCI-DSS Requirement 11.5 and SOC 2 security log standards.

---

## 📄 License
This project is open-source and intended for academic, bootcamp, and digital forensics training purposes.