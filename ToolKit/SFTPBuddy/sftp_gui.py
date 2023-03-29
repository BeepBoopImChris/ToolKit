import tkinter as tk
import subprocess
from modules.check_connection_source import check_connection_source
from modules.check_connection_destination import check_connection_destination
from modules.retrieve_files import retrieve_files_from_sftp

# Function to check source SFTP connection
def check_source_connection():
    # Get the values entered in the GUI input fields for the source SFTP server
    host = source_server_host.get()
    username = source_server_username.get()
    password = source_server_password.get()

    # Call the check_connection_source() function with the entered information
    if check_connection_source(host, username, password):
        # Change the color and text of the "Check Connection" button to green
        check_source_connection_button.config(fg='green', text='Connection Successful')
        
        # Enable the "Retrieve Files" and "On-going Transfer" buttons
        retrieve_files_button.config(state='normal')
        start_transfer_button.config(state='normal')
    else:
        # Change the color and text of the "Check Connection" button to red
        check_source_connection_button.config(fg='red', text='Connection Unsuccessful')
        
        # Disable the "Retrieve Files" and "On-going Transfer" buttons
        retrieve_files_button.config(state='disabled')
        start_transfer_button.config(state='disabled')

# Function to check destination SFTP connection
def check_destination_connection():
    # Get the values entered in the GUI input fields for the destination SFTP server
    host = destination_server_host.get()
    username = destination_server_username.get()
    password = destination_server_password.get()

    # Call the check_connection_destination() function with the entered information
    if check_connection_destination(host, username, password):
        # Change the color and text of the "Check Connection" button to green
        check_destination_connection_button.config(fg='green', text='Connection Successful')
        
        # Enable the "Retrieve Files" and "On-going Transfer" buttons
        retrieve_files_button.config(state='normal')
        start_transfer_button.config(state='normal')
    else:
        # Change the color and text of the "Check Connection" button to red
        check_destination_connection_button.config(fg='red', text='Connection Unsuccessful')
        
        # Disable the "Retrieve Files" and "On-going Transfer" buttons
        retrieve_files_button.config(state='disabled')
        start_transfer_button.config(state='disabled')

def retrieve_files_sftp():
    # Get the values entered in the GUI input fields for the destination SFTP server
    host = destination_server_host.get()
    username = destination_server_username.get()
    password = destination_server_password.get()
    folder = destination_server_folder.get()

    # Call the retrieve_files_from_sftp() function from the retrieve_files.py module with the entered information
    if retrieve_files_from_sftp(host, username, password, folder):
        # Change the color and text of the "Retrieve Files" button to green
        retrieve_files_button.config(fg='green', text='Success')
    else:
        # Change the color and text of the "Retrieve Files" button to red
        retrieve_files_button.config(fg='red', text='Error')


def start_transfer():
    # Get the values of the checkboxes
    daily_transfer = daily_checkbox_var.get()
    weekly_transfer = weekly_checkbox_var.get()
    
    # Create dictionary to store SFTP information
    sftp_info = {
        'source_server_host': source_server_host.get(),
        'source_server_username': source_server_username.get(),
        'source_server_password': source_server_password.get(),
        'source_server_folder': source_server_folder.get(),
        'destination_server_host': destination_server_host.get(),
        'destination_server_username': destination_server_username.get(),
        'destination_server_password': destination_server_password.get(),
        'destination_server_folder': destination_server_folder.get(),
        'transfer_frequency': ''
    }
    
    # Determine which transfer frequency checkbox was selected
    if daily_checkbox_var.get() == 1:
        sftp_info['transfer_frequency'] = 'Daily'
    elif weekly_checkbox_var.get() == 1:
        sftp_info['transfer_frequency'] = 'Weekly'
        
    # Print sftp_info
    print(sftp_info)
    
    # Launch the confirmation GUI process with the SFTP information
    command = ['python', 'modules/sftp_confirmation_gui.py', str(sftp_info)]
    print(f"Command being executed: {command}")
    subprocess.run(command)



root = tk.Tk()

daily_checkbox_var = tk.BooleanVar(value=False)
weekly_checkbox_var = tk.BooleanVar(value=False)

# Create input fields for source SFTP server
source_server_label = tk.Label(root, text="Source SFTP Server")
source_server_label.grid(row=0, column=0)

source_server_host_label = tk.Label(root, text="Host")
source_server_host_label.grid(row=1, column=0)

source_server_host = tk.Entry(root, width=30)
source_server_host.grid(row=2, column=0)

source_server_username_label = tk.Label(root, text="Username")
source_server_username_label.grid(row=3, column=0)

source_server_username = tk.Entry(root, width=30)
source_server_username.grid(row=4, column=0)

source_server_password_label = tk.Label(root, text="Password")
source_server_password_label.grid(row=5, column=0)

source_server_password = tk.Entry(root, width=30, show='*')
source_server_password.grid(row=6, column=0)

source_server_folder_label = tk.Label(root, text="Folder")
source_server_folder_label.grid(row=7, column=0)

source_server_folder = tk.Entry(root, width=30)
source_server_folder.grid(row=8, column=0)

# Create button to check source SFTP connection
check_source_connection_button = tk.Button(root, text="Check Connection", command=check_source_connection)
check_source_connection_button.grid(row=9, column=0)

# Create input fields for destination SFTP server
destination_server_label = tk.Label(root, text="Destination SFTP Server")
destination_server_label.grid(row=0, column=2)

destination_server_host_label = tk.Label(root, text="Host")
destination_server_host_label.grid(row=1, column=2)

destination_server_host = tk.Entry(root, width=30)
destination_server_host.grid(row=2, column=2)

destination_server_username_label = tk.Label(root, text="Username")
destination_server_username_label.grid(row=3, column=2)

destination_server_username = tk.Entry(root, width=30)
destination_server_username.grid(row=4, column=2)

destination_server_password_label = tk.Label(root, text="Password")
destination_server_password_label.grid(row=5, column=2)

destination_server_password = tk.Entry(root, width=30, show='*')
destination_server_password.grid(row=6, column=2)

destination_server_folder_label = tk.Label(root, text="Folder")
destination_server_folder_label.grid(row=7, column=2)

destination_server_folder = tk.Entry(root, width=30)
destination_server_folder.grid(row=8, column=2)

# Create button to check destination SFTP connection
check_destination_connection_button = tk.Button(root, text="Check Connection", command=check_destination_connection)
check_destination_connection_button.grid(row=9, column=2)

retrieve_files_button = tk.Button(root, text="Retrieve Files", command=retrieve_files_sftp, state='disabled')
retrieve_files_button.grid(row=10, column=1)

# Create button to start on-going transfer
start_transfer_button = tk.Button(root, text="On-going Transfer", command=start_transfer, state='disabled')
start_transfer_button.grid(row=11, column=1)

daily_checkbox = tk.Checkbutton(root, text="Daily", variable=daily_checkbox_var)
daily_checkbox.grid(row=12, column=0, padx=10, pady=10, sticky='w')
daily_checkbox.config(state='disabled')

weekly_checkbox = tk.Checkbutton(root, text="Weekly", variable=weekly_checkbox_var)
weekly_checkbox.grid(row=12, column=1, padx=10, pady=10, sticky='w')
weekly_checkbox.config(state='disabled')






root.mainloop()
