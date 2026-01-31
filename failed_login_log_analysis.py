import re

# Log file path
log_file = "log.txt"

# Regex pattern to match failed login attempts and extract IP address
pattern = re.compile(r"Failed login.*(\d+\.\d+\.\d+\.\d+)")

# Dictionary to store IP addresses and their failed attempt count
ip_count = {}

# Read the log file line by line
with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # remove extra spaces and newline
        match = pattern.search(line)
        
        # If the line contains a failed login, extract the IP
        if match:
            ip = match.group(1)
            ip_count[ip] = ip_count.get(ip, 0) + 1

# If any failed login attempts were found
if ip_count:
    print("Failed Login Attempts:")
    print("---------------------")

    # Print all IPs with their attempt count
    for ip, count in ip_count.items():
        print(ip, "=>", count)

    # Find the IP with the highest number of failed attempts
    top_ip = max(ip_count, key=ip_count.get)

    print("\nMost suspicious IP:")
    print(top_ip, "=>", ip_count[top_ip])

    # Write results to a report file
    with open("report.txt", "w", encoding="utf-8") as r:
        r.write("Failed Login Report\n")
        r.write("-------------------\n")

        for ip, count in ip_count.items():
            r.write(f"{ip} => {count}\n")

        r.write("\nMost suspicious IP:\n")
        r.write(f"{top_ip} => {ip_count[top_ip]}\n")

else:
    print("No failed login attempts found.")
