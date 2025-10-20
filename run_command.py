from SshToServer import SshToServer

def run_command(ssh_instance):
    command = input("Enter command to run on remote server: ")
    output, error = ssh_instance.runRemoteCommand(command)
    if error:
        print("Error:", error)
    else:
        print("Output:", output)

if __name__ == "__main__":
    my_ssh = SshToServer(r"C:\Users\lior-\Documents\GIT\Cloud-technologies\my-key-pair.pem", "13.53.193.221", "ubuntu")
    run_command(my_ssh)
