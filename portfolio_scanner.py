import os
import sys
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama for clean cross-platform colors
init(autoreset=True)

# 1. Design a custom ASCII Banner for your tool branding
BANNER = f"""
{Fore.CYAN}====================================================
  KALI RECON TOOL v1.0 | PORTFOLIO PROJECT
  Automated Network Availability & Logging Scanner
====================================================
"""

print(BANNER)

# 2. Grab the current live system timestamp
scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Scan initiated at: {scan_time}\n")

# Check if targets file exists before running
if not os.path.exists("targets.txt"):
    print(f"{Fore.RED}[!] Error: 'targets.txt' file not found. Please create it first.")
    sys.exit(1)

# 3. Open files to read inputs and log outputs
with open("targets.txt", "r") as infile, open("results.txt", "w") as outfile:

    # Write professional header metadata into the final report file
    outfile.write("====================================================\n")
    outfile.write(" KALI NETWORK SCAN REPORT \n")
    outfile.write(f" Generated on: {scan_time}\n")
    outfile.write("====================================================\n\n")

    for line in infile:
        target = line.strip()
        if not target:
            continue

        print(f"Scanning target: {target:<25}", end="", flush=True)

        # Execute network ping command
        response = os.system(f"ping -c 1 -W 1 {target} > /dev/null 2>&1")

        # 4. Handle results with clear visual color coding
        if response == 0:
            print(f"-> [{Fore.GREEN}ONLINE{Style.RESET_ALL}]")
            outfile.write(f"[{scan_time}] {target:<25} -> ONLINE\n")
        else:
            print(f"-> [{Fore.RED}OFFLINE/BLOCKED{Style.RESET_ALL}]")
            outfile.write(f"[{scan_time}] {target:<25} -> OFFLINE/BLOCKED\n")

print(f"\n{Fore.CYAN}[+] Scan completely finished! Detailed report saved to 'results.txt'.")
