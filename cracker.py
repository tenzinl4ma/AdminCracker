#!/usr/bin/env python3

import subprocess
import os
import time
import sys
import shutil
from pyfiglet import figlet_format


term_width = shutil.get_terminal_size().columns
print("-" * term_width + "\n")
print(figlet_format("DragonWarrior"))
print("-Developed by Tenzin".rjust(term_width))
print("-" * term_width + "\n")

WORDLIST = "/usr/share/wordlists/rockyou.txt"

import os

def is_fake_sudo():
    sudo_path = shutil.which("sudo")
    return os.path.realpath(sudo_path) == "/home/kali/bin/sudo"  #  you can put ur  clone sudo path here

def try_password(password):
    try:
        proc = subprocess.run(
            ["env", "FAKE_SUDO_MODE=brute", "sudo", "whoami"],
            input=password + "\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        return "Password correct." in proc.stdout
    except subprocess.TimeoutExpired:
        return False

def brute_force():
    with open(WORDLIST, "r", encoding="latin-1") as f:
        for count, line in enumerate(f, 1):
            pwd = line.strip()
            # Overwrite same line
            print(f"\rTrying Password #{count:>6}: {pwd[:30]:<30}", end='', flush=True)
            time.sleep(0)
            if try_password(pwd):
                print("\n" + "-" * term_width)
                print(f"[✓] Password Match found: {pwd}".center(term_width))
                print("-" * term_width + "\n")
                break
        else:
            print("\n" + "-" * term_width)
            print("[X] No match found.".center(term_width))
            print("-" * term_width + "\n")

if __name__ == "__main__":
    print("Starting brute-force attack...\n")
    if not is_fake_sudo():
        print("-" * term_width)
        print("[ERROR] The current 'sudo' is not the clone version.".center(term_width))
        print("First, clone and alias your fake sudo properly.".center(term_width))
        print("[ABORT] Refusing to bruteforce the real system binary.".center(term_width))
        print("-" * term_width + "\n")
        sys.exit(1)
    brute_force()

