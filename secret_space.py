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

# Function to display UI elements when device is connected
def show_connected():
    update_label_image("/home/oualid/Documents/piplo/zimage/connected_device.png")
    root.geometry("360x390")
    root.configure(bg="#141313")
    label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    canvas.config(bg="black")
    canvas.pack(side=tk.BOTTOM)

    # Display device information
    device_info = get_device_info()
    for i, info in enumerate(device_info):
        result_label = tk.Label(root, text=info, font=("Helvetica", 10, "bold"), bg="#787878", fg="white")
        result_label.place(relx=0.68, rely=0.10 + i * 0.08, anchor="center")
    
    # Show the Group3.png image
    image_label.place(relx=0.5, rely=0.18, anchor="center")

    # Show the check button
    check_button.place(relx=0.3, rely=0.35)

    # Show the Start button
    start_button_label.place(relx=0.35, rely=0.43)

