import os

print("Cyber SentinelX – Threat Correlation Engine\n")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

report_file = os.path.join(DATA_DIR, "final_report.txt")

def correlate():
    if not os.path.exists(report_file):
        print("No data to analyze.")
        return

    with open(report_file) as f:
        data = f.read()

    alerts = []

    if "Odd login time" in data:
        alerts.append("Suspicious login")

    if "Multiple failed logins" in data:
        alerts.append("Brute attempt")

    if "HIGH RISK" in data:
        alerts.append("Phishing activity")

    print("\n--- CORRELATION RESULT ---\n")

    if len(alerts) >= 2:
        print("⚠️ POSSIBLE ACCOUNT COMPROMISE DETECTED")
        print("Signals:", alerts)
    elif alerts:
        print("⚠️ Single anomaly detected:", alerts)
    else:
        print("System normal")

if __name__ == "__main__":
    correlate()