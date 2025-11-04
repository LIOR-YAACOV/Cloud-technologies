from SshToServer import SshToServer


if __name__ == "__main__":
    my_ssh = SshToServer(r"C:\Users\lior-\Documents\GIT\Cloud-technologies\my-key-pair.pem", "13.53.193.221", "ubuntu")
    file_name = input("Please enter the name of the file: ")
    seconds_to_wait = input("How many seconds to wait? ")
    command = f"./while_loops_bash/file_exists_check_daemon.sh {file_name} {seconds_to_wait} &"
    output, error = my_ssh.runRemoteCommand(command)
    if error:
        print("Error occurred:")
        print(error)
    else:
        print(output)