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
