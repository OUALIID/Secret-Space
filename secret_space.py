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

# Function to display UI elements when device is disconnected
def show_disconnected():
    update_label_image("/home/oualid/Documents/piplo/zimage/disconnected_device.png")
    root.geometry("360x250")
    root.configure(bg="#000000")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    canvas.pack_forget()

    # Hide the Group3.png image
    image_label.place_forget()

    # Hide the check button
    check_button.place_forget()
    
    # Hide device information labels
    hide_device_info()

    # Hide the Start button
    start_button_label.place_forget()

# Function to get device information
def get_device_info():
    properties = ["ro.product.manufacturer", "ro.product.model", "ro.serialno"]
    device_info = [subprocess.getoutput(f"adb shell getprop {prop} 2>/dev/null").strip() for prop in properties]

    if all(device_info):
        return device_info
    else:
        return []

# Function to hide device information labels
def hide_device_info():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget != label:
            widget.place_forget()

# Function to handle check button click event
def on_checkbutton_click():
    global check_button_clicked
    check_button_clicked = not check_button_clicked

# Function to handle start button click event
def on_start_button_click():
    output = subprocess.getoutput("adb shell getprop ro.product.manufacturer 2>/dev/null").strip()
    if check_button_clicked:
        if output == "vivo":
            activate_vivo_automatically()
    else:
        if output == "Xiaomi":
            activity_name = 'shell am start -n com.miui.securitycore/com.miui.securityspace.settings.SecondSpaceSettingActivity'
        elif output == "vivo":
            activity_name = 'shell am start -a android.settings.USER_SETTINGS'
        else:
            return
        run_adb_command_and_open_app(activity_name)

# Function to run ADB command and open app.
def run_adb_command_and_open_app(activity_name):
    command = f"adb -d {activity_name}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def tap_screen(x, y):
    command = f"shell input tap {x} {y}"
    run_adb_command_and_open_app(command)

def activate_vivo_automatically():
    run_adb_command_and_open_app('shell am start -a android.settings.USER_SETTINGS')
    time.sleep(2)
    tap_screen(900, 800)
    time.sleep(1)
    tap_screen(770, 2088)
    run_adb_command_and_open_app("shell input text user_2")
    time.sleep(1)
    tap_screen(1002, 174)
    time.sleep(7)
    tap_screen(770, 2088)
    time.sleep(1)
    tap_screen(555, 1106)
    time.sleep(1)
    tap_screen(770, 2088)

