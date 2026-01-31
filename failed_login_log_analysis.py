import re
from pathlib import Path

# File paths
LOG_FILE = "Python File Handling/log.txt"
REPORT_FILE = "report.txt"

# Regex pattern for failed login IPs
pattern = re.compile(r'Failed login.*(\d+\.\d+\.\d+\.\d+)')
ip_dict = {}

# Read and parse log file
try:
    with open(LOG_FILE, "r", encoding="utf-8") as log_file:
        for line in log_file:
            line = line.strip()
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                ip_dict[ip] = ip_dict.get(ip, 0) + 1
except FileNotFoundError:
    print(f"Error: {LOG_FILE} not found!")
    exit(1)

# Display results (sorted by count)
if ip_dict:
    print("Failed Login Attempts:")
    print("=" * 40)
    
    sorted_ips = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
    
    for ip, count in sorted_ips:
        print(f"{ip} => {count} attempts")
    
    # Most suspicious IP
    top_ip, top_count = sorted_ips[0]
    print(f"\nMost suspicious IP: {top_ip} => {top_count} attempts")
    
    # Write report
    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("Failed Login Report\n")
        report.write("=" * 40 + "\n\n")
        
        for ip, count in sorted_ips:
            report.write(f"{ip} => {count} attempts\n")
        
        report.write(f"\nMost suspicious IP:\n")
        report.write(f"{top_ip} => {top_count} attempts\n")
    
    print(f"\n✓ Report saved to {REPORT_FILE}")
else:
    print("No failed login attempts found!")