import pysftp

def retrieve_files_from_sftp(host, username, password, folder):
    try:
        # Create pysftp connection object
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        sftp = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)

        # Change directory to specified folder
        sftp.chdir(folder)

        # Retrieve files in folder
        files = sftp.listdir()

        # Download each file
        for file in files:
            local_file_path = "./downloads/" + file
            remote_file_path = folder + "/" + file
            sftp.get(remote_file_path, local_file_path)

        # Print success message
        print("Files retrieved")

        # Close connection
        sftp.close()

        return True

    except Exception as e:
        # Print error message
        print("Failed to retrieve files from destination SFTP server: " + str(e))

        return False
