import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

BANNER = f"""
{Fore.MAGENTA}==================================================================
  ADVANCED PORT SCANNER & BANNER GRABBER | PORTFOLIO PROJECT v2.0
  High-Performance Multi-Threaded Network Auditor
==================================================================
"""
print(BANNER)

# Target Assignment (Using Nmap's authorized test server)
TARGET_HOST = "scanme.nmap.org"
# Commonly audited ports for network vulnerabilities
PORTS_TO_SCAN = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3309, 8080]
MAX_THREADS = 10 # Simulating concurrency

try:
    TARGET_IP = socket.gethostbyname(TARGET_HOST)
except socket.gaierror:
    print(f"{Fore.RED}[!] Error: Could not resolve target hostname.")
    sys.exit(1)

print(f"Target Host : {TARGET_HOST} ({TARGET_IP})")
print(f"Scan Scope : Auditing {len(PORTS_TO_SCAN)} critical communication ports...")
print(f"Concurrency : Allocating {MAX_THREADS} worker threads...")
print(f"Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
print(f"{Fore.CYAN}{'PORT':<8}{'STATUS':<12}{'BANNER / SERVICE INFRASTRUCTURE'}")
print("-" * 66)

def audit_port(port):
    """Performs raw TCP handshake and service banner collection."""
    try:
        # 1. Establish a raw stream socket connection with a quick 2-second timeout
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)

        # 2. Attempt the TCP Three-Way Handshake connection
        result = s.connect_ex((TARGET_IP, port))

        if result == 0: # Connection Success
            # 3. Port is open; attempt to safely grab software banner information
            try:
                # Trigger a response from standard services (like HTTP/FTP)
                s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = s.recv(1024).decode('utf-8', errors='ignore').replace('\r', '').replace('\n', ' ').strip()
                # Clean up display constraints
                banner = banner[:40] if banner else "Open (No service banner emitted)"
            except socket.timeout:
                banner = "Open (Response timeout on banner request)"

            print(f"{Fore.GREEN}{port:<8}{'OPEN':<12}{Style.RESET_ALL}{banner}")
            s.close()
            return (port, "OPEN", banner)

        s.close()
    except Exception:
        pass
    return None

# 4. ThreadPool Execution Engine: Spreads the load over concurrent system workers
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    executor.map(audit_port, PORTS_TO_SCAN)

print("\n" + "=" * 66)
print(f"{Fore.MAGENTA}[+] Audit execution finished cleanly.")
