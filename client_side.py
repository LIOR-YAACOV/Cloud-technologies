from SshToServer import SshToServer
import pandas as pd
import json
import os

def run_command(ssh_instance):
    command = "python3 server_side.py"
    output, error = ssh_instance.runRemoteCommand(command)
    if error:
        return None
    else:
        return output

def updateCsv(data, filepath):
    df_new = pd.DataFrame([data], columns = list(data.keys()))
    cols = df_new.columns.tolist()
    df_new = df_new[[cols[-1]] + cols[:-1]]
    
    if not os.path.isfile(filepath):
        df_combined = df_new
    else:
        df_existing = pd.read_csv(filepath)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.to_csv(filepath, index=False)

if __name__ == "__main__":
    my_ssh = SshToServer(r"C:\Users\lior-\Documents\GIT\Cloud-technologies\my-key-pair.pem", "13.53.193.221", "ubuntu")
    data = run_command(my_ssh)
    if data:
        # data = data.strip().replace("'", '"')
        data = json.loads(data)
        updateCsv(data, "remote_log.csv")