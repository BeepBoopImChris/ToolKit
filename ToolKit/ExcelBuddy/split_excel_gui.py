
#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import tkinter as tk
from tkinter import filedialog, messagebox
from modules.split_excel import split_excel

class SplitExcelGUI:
    def __init__(self, master):
        self.master = master
        master.title("Split Excel")
        self.file_path = ""
        self.output_folder = ""
        self.num_splits = 0

        self.file_label = tk.Label(master, text="File: ")
        self.file_label.grid(row=0, column=0)

        self.output_label = tk.Label(master, text="Output Folder: ")
        self.output_label.grid(row=1, column=0)

        self.splits_label = tk.Label(master, text="Number of Splits: ")
        self.splits_label.grid(row=2, column=0)

        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.grid(row=0, column=1)

        self.output_entry = tk.Entry(master, width=50)
        self.output_entry.grid(row=1, column=1)

        self.splits_entry = tk.Entry(master, width=50)
        self.splits_entry.grid(row=2, column=1)

        self.file_button = tk.Button(master, text="Select File", command=self.upload_file)
        self.file_button.grid(row=0, column=2)

        self.output_button = tk.Button(master, text="Select Output Folder", command=self.select_output_folder)
        self.output_button.grid(row=1, column=2)

        self.split_button = tk.Button(master, text="Split File", command=self.split_file)
        self.split_button.grid(row=3, column=1)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, self.file_path)

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_folder)

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
        try:
            split_excel(self.file_path, self.num_splits, self.output_folder)
            messagebox.showinfo("Success", "File successfully split!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
gui = SplitExcelGUI(root)
root.mainloop()
