
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Toolbelt")

title_label = ttk.Label(window, text="Toolbelt")
title_label.pack(pady=30)

# Excel Buddy button
def open_excel_buddy():
    from ExcelBuddy import main_screen
    main_screen.open_main_screen()

def open_sftp_buddy():
    from SFTPBuddy import main_screen
    main_screen.open_main_screen()

excel_buddy_button = ttk.Button(window, text="Excel Buddy", command=open_excel_buddy)
excel_buddy_button.pack(pady=10)

# SFTP Buddy
sftp_buddy_button = ttk.Button(window, text="SFTP Buddy", command=open_sftp_buddy)
sftp_buddy_button.pack(pady=10)

window.geometry("500x300")
window.config(padx=50, pady=50)

window.mainloop()