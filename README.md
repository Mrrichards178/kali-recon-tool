# Network Reconnaissance & Compliance Logging Tool
A lightweight, automated network host discovery and availability scanner written in Python for Kali Linux.

## 📌 Project Overview
This project was developed as a portfolio piece to demonstrate fundamental concepts in **network automation**, **system scripting**, and **security logging**.

The tool processes an external target list, executes ICMP echo requests (pings) to analyze host states safely, handles multi-line anomalies, and compiles a time-stamped compliance audit report (`results.txt`) alongside a color-coded terminal view.

## 🚀 Key Features
* **Automated File I/O Integration:** Reads targets dynamically from a flat file (`targets.txt`) and handles empty space validation automatically.
* **Persistent Audit Logging:** Generates formal reports mapping out operational infrastructure status with structured formatting.
* **Deterministic Tracking:** Every logged item is tagged with a precise `YYYY-MM-DD HH:MM:SS` system timestamp.
* **Enhanced Visual Layouts:** Built-in error handling and a clean, color-coded UX using `colorama` to flag operational anomalies instantly.

## 🛠️ Requirements & Installation
This tool is optimized to run inside a **Kali Linux** environment.

1. Clone the repository or download the script file:
```bash
git clone https://github.com
cd kali-recon-tool
```

2. Install the necessary Python packages:
```bash
pip3 install colorama --break-system-packages
```

## 💻 Usage Instructions
1. Create a `targets.txt` file in the same directory and populate it with the IP addresses or hostnames you want to inventory (one per line):
```text
google.com
8.8.8.8
wikipedia.org
```

2. Execute the core Python tool:
```bash
python3 portfolio_scanner.py
```

## 📊 Sample Output
### Terminal Interface
```text
====================================================
  KALI RECON TOOL v1.0 | PORTFOLIO PROJECT
  Automated Network Availability & Logging Scanner
====================================================

Scan initiated at: 2026-07-14 19:40:12

Scanning target: google.com -> [ONLINE]
Scanning target: 8.8.8.8 -> [ONLINE]
Scanning target: invalid-target-test.xyz -> [OFFLINE/BLOCKED]

[+] Scan completely finished! Detailed report saved to 'results.txt'.
```

### Generated Audit Report (`results.txt`)
```text
====================================================
            KALI NETWORK SCAN REPORT
Generated on: 2026-07-14 19:40:12
====================================================

[2026-07-14 19:40:12] google.com -> ONLINE
[2026-07-14 19:40:13] 8.8.8.8 -> ONLINE
[2026-07-14 19:40:14] invalid-target-test.xyz -> OFFLINE/BLOCKED
```

---
*Developed by [MARK] as part of a Cybersecurity & Linux Infrastructure study portfolio.*
