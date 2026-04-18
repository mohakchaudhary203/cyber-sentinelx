import os
import time
import subprocess

print("Cyber SentinelX – Live Monitoring Mode\n")

last_size = 0

while True:
    path = "data/login_log.txt"

    if os.path.exists(path):
        size = os.path.getsize(path)

        if size != last_size:
            print("New activity detected!")
            subprocess.run(["python", "core/soc_detector.py"])
            last_size = size

    time.sleep(5)