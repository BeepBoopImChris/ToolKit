import paramiko

class sftp_que_func:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.transport = None
        self.sftp = None

    def open_connection(self):
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = self.transport.open_sftp()

    def put_file(self, local_path, remote_path):
        if self.sftp is None:
            self.open_connection()
        self.sftp.put(local_path, remote_path)

    def close_connection(self):
        if self.sftp is not None:
            self.sftp.close()
        if self.transport is not None:
            self.transport.close()

#TODO Error handling for connection time out, and incorrect login credentials