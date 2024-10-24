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

