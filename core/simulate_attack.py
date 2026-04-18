import random
from datetime import datetime

print("="*60)
print("Cyber SentinelX – Adaptive Threat Monitoring Platform")
print("Attack Simulation Module")
print("="*60)

print("\nSelect Attack Scenario:")
print("1. Insider Threat (odd time login)")
print("2. Login Attack Burst (multiple failures)")
print("3. Phishing URL Injection")

choice = input("\nEnter choice: ")

# FILE PATHS
LOGIN_FILE = "data/login_log.txt"
FAILED_FILE = "data/failed_log.txt"
URL_FILE = "data/urls.txt"


def insider_threat():
    print("\n[Simulating Insider Threat...]")

    with open(LOGIN_FILE, "a") as f:
        for i in range(3):
            hour = random.randint(0, 5)  # odd hours
            time = f"{hour}:15:00"
            f.write(f"user{i},{time}\n")

    print("Odd-hour logins generated.")


def login_burst():
    print("\n[Simulating Brute Login Attack...]")

    with open(FAILED_FILE, "a") as f:
        for i in range(5):
            time = datetime.now().strftime("%H:%M:%S")
            f.write(f"attacker,{time}\n")

    print("Multiple failed logins generated.")


def phishing_attack():
    print("\n[Simulating Phishing Attack...]")

    urls = [
        "http://secure-login-alert.com",
        "http://verify-account-now.com",
        "http://bank-login-secure.net"
    ]

    with open(URL_FILE, "a") as f:
        for url in urls:
            f.write(url + "\n")

    print("Suspicious URLs added.")


# RUN SCENARIO
if choice == "1":
    insider_threat()
elif choice == "2":
    login_burst()
elif choice == "3":
    phishing_attack()
else:
    print("Invalid choice.")