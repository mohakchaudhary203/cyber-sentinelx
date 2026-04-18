import subprocess

print("Cyber SentinelX – Adaptive Threat Monitoring Platform\n")

print("1. Run Attack Simulation")
print("2. Run Detection Only")
print("3. Start Live Monitoring")

choice = input("Select option: ")

if choice == "1":
    subprocess.run(["python", "core/simulate_attack.py"])
    subprocess.run(["python", "core/soc_detector.py"])
    subprocess.run(["python", "core/url_analyzer.py"])

elif choice == "2":
    subprocess.run(["python", "core/soc_detector.py"])
    subprocess.run(["python", "core/url_analyzer.py"])

elif choice == "3":
    subprocess.run(["python", "core/live_monitor.py"])

else:
    print("Invalid choice")