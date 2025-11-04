from run_local_command import run_local_command
import json

def get_logs_info(file):
    log_dict = {"ERROR": 0, "INFO": 0, "WARN": 0}
    with open(file, "r") as f:
        for line in f.readlines():
            words = line.split()
            if len(words) > 5:
                severity = line.split()[5]
                if severity in log_dict:
                    log_dict[severity] += 1
    timestamp = run_local_command("date +%s")[0].strip()
    log_dict["timestamp"] = timestamp
    log_string = json.dumps(log_dict)
    return log_string
    
if __name__ == "__main__":
    file = "/var/log/syslog"
    logs_info = get_logs_info(file)
    print(logs_info)
