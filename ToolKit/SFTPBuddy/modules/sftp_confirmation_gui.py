import tkinter as tk
from tkinter import ttk

class SFTPConfirmationGUI:
    def __init__(self, source_host, source_username, source_folder, destination_host, destination_username, destination_folder, frequency):
        # Create root window
        self.root = tk.Tk()
        self.root.title("SFTP Confirmation")

        # Create labels to display SFTP information
        source_info_label = tk.Label(self.root, text="Source SFTP Information:")
        source_info_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        source_host_label = tk.Label(self.root, text="Host: {}".format(source_host))
        source_host_label.grid(row=1, column=0, sticky="w", padx=20)

        source_username_label = tk.Label(self.root, text="Username: {}".format(source_username))
        source_username_label.grid(row=2, column=0, sticky="w", padx=20)

        source_folder_label = tk.Label(self.root, text="Folder: {}".format(source_folder))
        source_folder_label.grid(row=3, column=0, sticky="w", padx=20)

        destination_info_label = tk.Label(self.root, text="Destination SFTP Information:")
        destination_info_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        destination_host_label = tk.Label(self.root, text="Host: {}".format(destination_host))
        destination_host_label.grid(row=5, column=0, sticky="w", padx=20)

        destination_username_label = tk.Label(self.root, text="Username: {}".format(destination_username))
        destination_username_label.grid(row=6, column=0, sticky="w", padx=20)

        destination_folder_label = tk.Label(self.root, text="Folder: {}".format(destination_folder))
        destination_folder_label.grid(row=7, column=0, sticky="w", padx=20)

        frequency_label = tk.Label(self.root, text="Transfer Frequency: {}".format(frequency))
        frequency_label.grid(row=8, column=0, sticky="w", padx=20, pady=20)

        # Create confirmation button
        confirm_button = ttk.Button(self.root, text="Confirm", command=self.confirm)
        confirm_button.grid(row=9, column=0, pady=10)

        # Disable the button by default
        confirm_button.state(['disabled'])

        # Start the main loop
        self.root.mainloop()

    def confirm(self):
        # Function to be called when the Confirm button is clicked
        print("Confirmed")
