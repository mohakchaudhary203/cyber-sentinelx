import os
import time

print("Cyber SentinelX – Live Monitoring Module\n")

LOG_FILE = "data/live_activity.txt"

def monitor():
    print("Monitoring system activity... (Ctrl+C to stop)\n")

    # simulate reading system activity (safe version)
    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE) as f:
                lines = f.readlines()

            if len(lines) > 0:
                last = lines[-1]

                if "failed" in last.lower():
                    print("⚠️ Failed activity detected:", last.strip())

                if "admin" in last.lower():
                    print("⚠️ Privileged access detected:", last.strip())

        time.sleep(3)


if __name__ == "__main__":
    monitor()