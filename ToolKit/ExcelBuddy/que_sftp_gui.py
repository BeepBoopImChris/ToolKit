import os
import tkinter as tk
from tkinter import filedialog, messagebox
from modules.sftp_que_func import sftp_que_func
from modules.sftp_progress_window import SftpUploadProgress
import time

class SftpUploader:
    def __init__(self, master):
        self.master = master
        master.title("SFTP Uploader")

        # Labels and entries for the GUI
        tk.Label(master, text="Folder Path:").grid(row=0, column=0, padx=10, pady=10)
        self.folder_entry = tk.Entry(master, width=60)
        self.folder_entry.grid(row=0, column=1, padx=10, pady=10)

        browse_button = tk.Button(master, text="Browse", command=self.browse_folder, width=10)
        browse_button.grid(row=0, column=2, padx=10, pady=10)

        tk.Label(master, text="Username:").grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(master, width=60)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(master, text="Password:").grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(master, width=60, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(master, text="Host:").grid(row=3, column=0, padx=10, pady=10)
        self.host_entry = tk.Entry(master, width=60)
        self.host_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(master, text="Port:").grid(row=4, column=0, padx=10, pady=10)
        self.port_entry = tk.Entry(master, width=60)
        self.port_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(master, text="Remote Directory:").grid(row=5, column=0, padx=10, pady=10)
        self.remote_dir_entry = tk.Entry(master, width=60)
        self.remote_dir_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(master, text="Delay in Minutes:").grid(row=6, column=0, padx=10, pady=10)
        self.delay_entry = tk.Entry(master, width=60)
        self.delay_entry.grid(row=6, column=1, padx=10, pady=10)

        upload_button = tk.Button(master, text="Upload", command=self.upload_files, width=10)
        upload_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.master.deiconify()

    def browse_folder(self):
        folder_path = filedialog.askdirectory(initialdir='/', message='Please select a directory')
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(tk.END, folder_path)

    def upload_files(self):
        folder_path = self.folder_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        host = self.host_entry.get()
        port = self.port_entry.get()
        remote_dir = self.remote_dir_entry.get()
        delay_time = int(self.delay_entry.get())

        if not all((folder_path, username, password, host, port, remote_dir)):
            messagebox.showwarning("Warning", "Please fill in all fields.")
            return

        sftp = sftp_que_func(host, port, username, password)

        num_files_uploaded = 0
        num_files_failed = 0

        try:
            files = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to list files in folder:\n{str(e)}")
            return

        for file_path in files:
            if not os.path.isfile(file_path):
                continue

            try:
                sftp.put_file(file_path, remote_dir)
                num_files_uploaded += 1
            except Exception as e:
                print(f"Failed to upload file {file_path}: {str(e)}")
                num_files_failed += 1

            time.sleep(delay_time*60)

        sftp.close_connection()

        result_message = f"{num_files_uploaded} files uploaded successfully."

        if num_files_failed > 0:
            result_message += f"\n{num_files_failed} files failed to upload."

        messagebox.showinfo("Info", result_message)
        
        # Open progress window after upload is complete
        SftpUploadProgress(username)


if __name__ == "__main__":
    root = tk.Tk()
    app = SftpUploader(root)
    root.mainloop()
    print("Program finished")


#TODO, On the right hand side of the GUI, update the outcome as info is types. Full process time, amount of files, ect...
