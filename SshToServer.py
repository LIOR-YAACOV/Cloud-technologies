import paramiko

class SshToServer:
    def __init__(self, pem_file_path, host, username):
        '''
        pem_file_path : path to key pair file
        host : ip address
        username : ubuntu
        '''
        self.pem_file_path = pem_file_path
        self.host = host
        self.username = username
        self.sshClient = paramiko.SSHClient()
        # class to make ssh connection
        self.connect()

    def connect(self):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(self.pem_file_path)
        self.sshClient.connect(hostname=self.host, username=self.username, pkey=private_key)

    def runRemoteCommand(self, command):
        # command : command to run on remote server
        try:   
            stdin, stdout, stderr = self.sshClient.exec_command(command) # tuple ( , , )
            output = stdout.read().decode()
            error = stderr.read().decode()
            return output, error
        except Exception as e:
            print(f"An error occurred: {e}")
