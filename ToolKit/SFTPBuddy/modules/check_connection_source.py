import pysftp

def check_connection_source(host, username, password):
    try:
        # Create pysftp connection object
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        sftp = pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts)

        # Print success message
        print("Connection to source SFTP server successful")

        # Close connection
        sftp.close()

        return True

    except Exception as e:
        # Print error message
        print("Connection to source SFTP server failed: " + str(e))

        return False
