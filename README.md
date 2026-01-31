# 🔐 Failed Login Analyzer

A Python-based security tool that analyzes server log files to detect and report suspicious failed login attempts by tracking IP addresses.

## 📋 Features

- ✅ Parses log files for failed login attempts
- ✅ Extracts and counts IP addresses
- ✅ Identifies most suspicious IP addresses
- ✅ Generates detailed security reports
- ✅ Sorted output by attempt frequency
- ✅ Error handling for missing files



## 📁 Project Structure

```
failed-login-analyzer/
│
├── analyzer.py              # Main script
│──   log.txt                # log file (sample included)
├── report.txt              # Generated report (auto-created)




## 🛠️ Technical Details

### Regular Expression Pattern
```python
r'Failed login.*(\d+\.\d+\.\d+\.\d+)'
```
This pattern matches any line containing "Failed login" followed by an IPv4 address.

### Key Components

- **IP Tracking**: Dictionary-based counting for efficient lookup
- **Sorting**: Results sorted by attempt count (descending)
- **File Handling**: UTF-8 encoding support for international characters
- **Error Handling**: Graceful handling of missing files



## 📈 Use Cases

- 🔒 **Security Auditing**: Identify brute force attack attempts
- 📊 **Traffic Analysis**: Monitor failed authentication patterns
- 🚨 **Intrusion Detection**: Detect suspicious IP addresses
- 📝 **Compliance Reporting**: Generate security incident reports




⭐ **If you find this project helpful, please consider giving it a star!** ⭐
