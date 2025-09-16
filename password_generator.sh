#!/bin/bash
# Password Generator CLI for Linux 
# Author: Sudo-xdk (Dhanush)
# GitHub: https://github.com/Sudo-xdk

# Check for figlet
if ! command -v figlet &> /dev/null
then
    echo "figlet not found. Installing..."
    sudo apt install figlet -y
fi

# Display ASCII banner
figlet -f slant "Pass_Gen CLI"

# Display author info
echo -e "\033[1;34mAuthor: Sudo-xdk (Dhanush) | GitHub: https://github.com/Sudo-xdk\033[0m"

# Display secure password message
echo -e "\033[1;32m🔐 Secure Password Generator CLI\033[0m"
echo ""

# Check if Python script exists
PYTHON_SCRIPT="password_generator.py"
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: $PYTHON_SCRIPT not found in current directory!"
    exit 1
fi

# Run Python script with all provided arguments
python3 "$PYTHON_SCRIPT" "$@"
