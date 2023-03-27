import tkinter as tk

class SftpUploadProgress:
    def __init__(self, username, remote_dir):
        self.root = tk.Toplevel()
        self.root.title("SFTP Upload Progress")

        self.username_label = tk.Label(self.root, text=f"Uploading as user: {username}")
        self.username_label.pack(pady=10)

        self.remote_dir_label = tk.Label(self.root, text=f"Uploading to remote directory: {remote_dir}")
        self.remote_dir_label.pack(pady=10)

        self.progress_bar = tk.ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=20)

        self.bytes_label = tk.Label(self.root, text="0 bytes")
        self.bytes_label.pack(pady=5)

        self.speed_label = tk.Label(self.root, text="0 KB/s")
        self.speed_label.pack(pady=5)

        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel_upload)
        self.cancel_button.pack(pady=20)

    def update_progress(self, bytes_sent, file_size, speed):
        self.progress_bar["value"] = (bytes_sent / file_size) * 100
        self.bytes_label.config(text=f"{bytes_sent} / {file_size} bytes")
        self.speed_label.config(text=f"{speed:.2f} KB/s")

    def cancel_upload(self):
        self.root.destroy()
