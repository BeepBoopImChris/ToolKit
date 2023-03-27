#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import tkinter as tk
from tkinter import filedialog, messagebox
import codecs
import pandas as pd
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
from modules.split_excel import split_excel

class SplitExcelGUI:
    def __init__(self, master):
        self.master = master
        master.title("Split Excel")
        self.file_path = ""
        self.output_folder = ""
        self.num_splits = 0

        # File selection widgets
        self.file_label = tk.Label(master, text="File:")
        self.file_label.grid(row=0, column=0, sticky="e")
        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)
        self.file_button = tk.Button(master, text="Select File", command=self.upload_file)
        self.file_button.grid(row=0, column=2, padx=5, pady=5)

        # Output folder selection widgets
        self.output_label = tk.Label(master, text="Output Folder:")
        self.output_label.grid(row=1, column=0, sticky="e")
        self.output_entry = tk.Entry(master, width=50)
        self.output_entry.grid(row=1, column=1, padx=5, pady=5)
        self.output_button = tk.Button(master, text="Select Output Folder", command=self.select_output_folder)
        self.output_button.grid(row=1, column=2, padx=5, pady=5)

        # Number of splits widgets
        self.splits_label = tk.Label(master, text="Number of Splits:")
        self.splits_label.grid(row=2, column=0, sticky="e")
        self.splits_entry = tk.Entry(master, width=50)
        self.splits_entry.grid(row=2, column=1, padx=5, pady=5)

        # Rows per file widgets
        self.rows_label = tk.Label(master, text="Rows per File:")
        self.rows_label.grid(row=3, column=0, sticky="e")
        self.rows_value = tk.StringVar()
        self.rows_value.set("N/A")
        self.rows_entry = tk.Entry(master, width=50, state="readonly", textvariable=self.rows_value)
        self.rows_entry.grid(row=3, column=1, padx=5, pady=5)

        # Split file button
        self.split_button = tk.Button(master, text="Split File", command=self.split_file)
        self.split_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)


    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, self.file_path)
        self.calculate_rows_per_file()

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_folder)

    def calculate_rows_per_file(self):
        if not self.file_path:
            return
        if self.num_splits == 0:
            return
        try:
            df = pd.read_excel(self.file_path)
            num_rows = len(df) - 1  # exclude the header row
            self.rows_per_file = num_rows // self.num_splits
            self.rows_leftover = num_rows % self.num_splits
            self.rows_value.set(self.rows_per_file)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def split_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file to split.")
            return
        if not self.output_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return
        try:
            self.num_splits = int(self.splits_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of splits.")
            return
        if self.num_splits <= 0:
            messagebox.showerror("Error", "Number of splits must be greater than zero.")
            return

        self.calculate_rows_per_file()

        try:
            split_excel(self.file_path, self.num_splits, self.output_folder)
            messagebox.showinfo("Success", "File successfully split!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
gui = SplitExcelGUI(root)
root.mainloop()
