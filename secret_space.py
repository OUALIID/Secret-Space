#!/usr/bin/python3

import tkinter as tk
import subprocess
import time

# Global variables
check_button_clicked = False

# Function to update label image
def update_label_image(image_path):
    global image
    image = tk.PhotoImage(file=image_path)
    label.config(image=image)
    label.image = image
    label.lift()

# Function to update label according to device connection status
def update_label():
    output = subprocess.getoutput("adb get-state 2>/dev/null").strip()
    if output == "device":
        show_connected()
    else:
        show_disconnected()
    root.after(1000, update_label)

