# Source file

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#Entry point
root=tk.Tk()
root.title('Updater')
root.geometry("800x500")

#image part
img_open = Image.open("F:/Projects/Updater/sources/logo_debian.png")
resized = img_open.resize((200, 120), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(resized)
image_label = tk.Label(root,image=logo)
image_label.pack(pady=10, padx=10, anchor="w")
#image_label.grid(padx=50,pady=1)

# Data Fetching
data_os = tk.Label(root, text="OS Name")
data_os.pack(pady=10, padx=10, anchor="w")

data_version =tk.Label(root, text=" Kernal Version")
data_version.pack(pady=10, padx=10, anchor="w")

total_intalled_apps = tk.Label(root, text='Total Installed Apps')
total_intalled_apps.pack(pady=10, padx=10, anchor="w")

uptodated_apps = tk.Label(root, text='Upto-dated Apps')
uptodated_apps.pack(pady=10, padx=10, anchor="w")

avaialble_update = tk.Label(root, text='Available Updated')
avaialble_update.pack(pady=10, padx=10, anchor="w")

# Button and Toggles
update_button = tk.Button(root, text='Update', width=30, command=root.destroy)
update_button.pack(pady=5)

# Line
canvas = Canvas(root)
canvas.create_line(5, 150, 2000, 150, width=1)
#canvas.pack()

#Update Info
system_status = tk.Label(root, text="System status")
system_status.pack(pady=10, padx=10, anchor="w")

last_update = tk.Label(root, text="Last Update")
last_update.pack(pady=10, padx=10, anchor="e")


root.mainloop()
