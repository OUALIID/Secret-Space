#!/bin/bash

BASE_DIR=$(dirname "$(realpath "$0")")
SCRIPT_PATH="$BASE_DIR/zzz.py"
ICON_PATH="$BASE_DIR/zimage/Icon.png"
DESKTOP_FILE="$HOME/.local/share/applications/SecretSpace.desktop"

# Step 1: Check for Python3 installation
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt update
    sudo apt install -y python3
else
    echo "Python3 is already installed."
fi

# Step 2: Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed. Installing pip..."
    sudo apt install -y python3-pip
else
    echo "pip is already installed."
fi

# Step 3: Check for required Python modules
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Tkinter is not installed. Installing Tkinter using pip..."
    pip3 install tk
else
    echo "Tkinter is already installed."
fi

# Step 4: Create a .desktop file for the application in the applications directory
echo "Creating desktop entry at $DESKTOP_FILE..."
{
    echo "[Desktop Entry]"
    echo "Version=1.0"
    echo "Type=Application"
    echo "Name=Secret Space"
    echo "Comment=Launch Secret Space application"
    echo "Exec=python3 $SCRIPT_PATH"
    echo "Icon=$ICON_PATH"
    echo "Terminal=false"
    echo "Categories=Utility;"
    echo "StartupNotify=true"
} > "$DESKTOP_FILE"

chmod +x "$DESKTOP_FILE"

# Verify that the desktop file was created successfully
if [[ -f "$DESKTOP_FILE" ]]; then
    echo "Desktop file created successfully."
else
    echo "Failed to create desktop file. Please check permissions and paths."
fi

echo "Setup complete! You can now run Secret Space from your applications menu."
