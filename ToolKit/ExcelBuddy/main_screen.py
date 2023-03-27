import tkinter as tk
import subprocess

def open_split_excel():
    subprocess.Popen(["python3", "ExcelBuddy/split_excel_gui.py"])

def open_sftp_que_upload():
    subprocess.Popen(["python3", "ExcelBuddy/que_sftp_gui.py"])

window = tk.Tk()
window.title("Excel Buddy")

title_label = tk.Label(window, text="Excel Buddy", font=("Arial", 20))
title_label.pack(pady=(25, 0))

# Excel File button
split_file_button = tk.Button(window, text="Split Excel", command=open_split_excel)
split_file_button.pack(pady=10)

#SFTP Upload Button
sftp_upload_button = tk.Button(window, text="Que SFTP Upload", command=open_sftp_que_upload)
sftp_upload_button.pack(pady=10)

window.mainloop()
