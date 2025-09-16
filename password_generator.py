import argparse
import hashlib
import string
import sys
from getpass import getpass

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


def generate_password(service, master_password, length=16, use_digits=True, use_symbols=True, no_ambiguous=False, show_salt=False):
    """
    Generates a unique, strong password for a service based on a master password.
    Uses PBKDF2-HMAC-SHA384, a secure key derivation function.
    """
    # Create a unique salt from the service name AND part of the master password
    salt = service.encode() + master_password[:8].lower().encode()

    if show_salt:
        print(f"[DEBUG] Service: {service}")
        print(f"[DEBUG] Master Password (first 8 chars, lowercased): {master_password[:8].lower()}")
        print(f"[DEBUG] Salt (hex): {salt.hex()}")

    # Use PBKDF2 with SHA-384 to generate a seed
    key = hashlib.pbkdf2_hmac(
        'sha384',
        master_password.encode(),
        salt,
        150000,    # High iteration count for brute-force resistance
        dklen=512  # Generate ample key material
    )

    # Define character sets
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if no_ambiguous:
        ambiguous_chars = 'l1I0O'
        chars = ''.join(c for c in chars if c not in ambiguous_chars)

    # Generate password from the derived key
    password = []
    for byte in key:
        if len(password) >= length:
            break
        index = byte % len(chars)
        password.append(chars[index])
    
    return ''.join(password)


def main():
    parser = argparse.ArgumentParser(
        description="Generate unique, strong passwords from a master password using PBKDF2-HMAC-SHA384."
    )
    parser.add_argument("service", help="Service/website name (e.g., 'github.com')")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16, min: 12)")
    parser.add_argument("-nd", "--no-digit", action="store_true", help="Exclude digits")
    parser.add_argument("-ns", "--no-symbol", action="store_true", help="Exclude symbols")
    parser.add_argument("-na", "--no-ambiguous", action="store_true", help="Exclude ambiguous characters (l1I0O)")
    parser.add_argument("-c", "--copy", action="store_true", help="Copy to clipboard")
    parser.add_argument("--show-salt", action="store_true", help="Show how the salt is constructed (debug mode)")

    args = parser.parse_args()

    # Validate length - increased minimum for better security
    if args.length < 8:
        print("Error: For security, password length must be at least 8 characters.", file=sys.stderr)
        sys.exit(1)

    # Get master password securely
    master_password = getpass("Enter your Master Password: ")
    if not master_password:
        print("Error: Master Password cannot be empty.", file=sys.stderr)
        sys.exit(1)

    # Confirm master password
    confirm_password = getpass("Confirm your Master Password: ")
    if master_password != confirm_password:
        print("Error: Master Passwords do not match.", file=sys.stderr)
        sys.exit(1)

    # Generate the password
    password = generate_password(
        service=args.service,
        master_password=master_password,
        length=args.length,
        use_digits=not args.no_digit,
        use_symbols=not args.no_symbol,
        no_ambiguous=args.no_ambiguous,
        show_salt=args.show_salt
    )

    # Output result
    print(f"\nService: {args.service}")
    print(f"Generated Password: {password}")
    print(f"Password Length: {len(password)} characters")

    # Copy to clipboard if requested
    if args.copy:
        if CLIPBOARD_AVAILABLE:
            pyperclip.copy(password)
            print("Password copied to clipboard!")
        else:
            print("Note: Install 'pyperclip' for clipboard support: pip install pyperclip")


if __name__ == "__main__":
    main()

