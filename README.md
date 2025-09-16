# 🔐 Password Generator CLI

A secure command-line tool to generate unique, strong, and deterministic passwords for different services using a **master password**.  
Passwords are derived with **PBKDF2-HMAC-SHA384** and can optionally be copied to the clipboard.

---

## Features
- Deterministic password generation (same service + master password → same result).
- Secure key derivation using **PBKDF2-HMAC-SHA384** with 150,000 iterations.
- Option to exclude digits, symbols, or ambiguous characters (`l1I0O`).
- Debug mode to inspect salt construction (`--show-salt`).
- Clipboard support (via `pyperclip`).
- Works on Linux, macOS, and Windows.
---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sudo-xdk/Password-Generator-CLI.git
cd Password-Generator-CLI
```
## Windows / macOS
Install Python packages:

```bash
pip install -r requirements.txt
```
Run the Python script:
```bash
python password_generator.py --help
```
## Linux Users
Option 1: Install system dependencies manually:
```bash
sudo apt update
sudo apt install figlet toilet python3 python3-pip -y
```
Option 2: Use the helper script to install dependencies automatically:

```bash
./install_deps.sh
```
Install Python packages:
```bash
pip3 install -r requirements.txt
```
Run the script:
```bash
./password_generator.sh github.com
```
⚡ Usage
Basic Example
```bash
python password_generator.py github.com
```
You’ll be prompted for your master password and confirmation, then a password will be generated.

Custom Length
```bash
python password_generator.py github.com -l 24
```
Exclude Digits or Symbols
```bash
python password_generator.py twitter.com --no-digit --no-symbol
```
Exclude Ambiguous Characters
```bash
python password_generator.py gmail.com --no-ambiguous
```
Debug Salt Construction
```bash
python password_generator.py reddit.com --show-salt
```
Copy to Clipboard
```bash
python password_generator.py linkedin.com -c
```
⚠️ Requires pyperclip.

🔒 Security Notes
Master password is never stored.

Salt is derived from service name + first 8 characters of your master password (lowercased).

Minimum password length is enforced (8+ characters).

Uses PBKDF2-HMAC-SHA384 with 150,000 iterations and 512 bytes of derived key material.
