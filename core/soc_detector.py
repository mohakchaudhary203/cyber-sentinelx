import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def soc_analysis():
    risk = 0
    alerts = []

    login_file = os.path.join(DATA_DIR, "login_log.txt")
    failed_file = os.path.join(DATA_DIR, "failed_log.txt")
    report_file = os.path.join(DATA_DIR, "final_report.txt")
    live_file = os.path.join(DATA_DIR, "live_activity.txt")

    os.makedirs(DATA_DIR, exist_ok=True)

    logs = open(login_file).readlines() if os.path.exists(login_file) else []
    failed = open(failed_file).readlines() if os.path.exists(failed_file) else []

    # 🔥 RULE 1: Odd login time
    for log in logs:
        try:
            user, time = log.strip().split(",")
            hour = int(time.split(":")[0])

            if hour < 6 or hour > 22:
                alerts.append((user, "Odd login time", "MEDIUM"))
                risk += 30
        except:
            continue

    # 🔥 RULE 2: Multiple failed logins
    if len(failed) >= 3:
        alerts.append(("SYSTEM", "Multiple failed logins", "HIGH"))
        risk += 50

    # 🔥 WRITE REPORT
    with open(report_file, "w") as f:
        for a in alerts:
            f.write(str(a) + "\n")
        f.write(f"Risk Score: {risk}")

    # 🔥 LIVE ALERT FEED
    with open(live_file, "a") as live:
        for a in alerts:
            live.write(f"ALERT: {a}\n")

    print("SOC Analysis Complete.")


if __name__ == "__main__":
    soc_analysis()