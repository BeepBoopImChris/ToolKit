import tkinter as tk
import subprocess

def open_sftp_connection():
    subprocess.Popen(["python3", "ToolKit/SFTPBuddy/sftp_gui.py"])

window = tk.Tk()
window.title("SFTP Buddy")

title_label = tk.Label(window, text="SFTP Buddy", font=("Arial", 20))
title_label.pack(pady=(25, 0))

# SFTP Connection Button
split_file_button = tk.Button(window, text="Connect SFTP's", command=open_sftp_connection)
split_file_button.pack(pady=10)

window.mainloop()
