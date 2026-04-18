from flask import Flask, render_template, redirect, url_for, request, session
import os
import subprocess
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "final_report.txt")
USERS_FILE = os.path.join(BASE_DIR, "data", "users.txt")


# ---------------- USERS ----------------
def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE) as f:
            for line in f:
                u, p = line.strip().split(",")
                users[u] = p
    return users


def save_user(u, p):
    with open(USERS_FILE, "a") as f:
        f.write(f"{u},{p}\n")


# ---------------- LOGIN ----------------
import hashlib

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = hash_password(request.form["password"])

        if os.path.exists(USERS_FILE):
            with open(USERS_FILE) as f:
                for line in f:
                    user, stored = line.strip().split(",")
                    if user == u and stored == p:
                        session["user"] = u
                        return redirect(url_for("home"))

    return render_template("login.html")

# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        u = request.form["username"]
        p = hash_password(request.form["password"])

        with open(USERS_FILE, "a") as f:
            f.write(f"{u},{p}\n")

        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# ---------------- DASHBOARD ----------------
def parse():
    alerts = []
    risk = 0

    if os.path.exists(DATA_PATH):
        lines = open(DATA_PATH).readlines()

        for line in lines:
            if "Risk Score" in line:
                try:
                    risk = int(line.split(":")[1])
                except:
                    risk = 0
            else:
                alerts.append(line.strip())

    return alerts, risk


@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    alerts, risk = parse()

    status = "NORMAL"
    if risk >= 100:
        status = "CRITICAL"
    elif risk >= 50:
        status = "WARNING"

    # 🔥 CORRELATION
    correlation = "System Normal"
    if len(alerts) >= 2:
        correlation = "⚠️ Possible Account Compromise"

    return render_template(
        "index.html",
        alerts=alerts,
        risk=risk,
        status=status,
        timestamp=datetime.now().strftime("%H:%M:%S"),
        alert_count=len(alerts),
        correlation=correlation
    )


# ---------------- ATTACK ----------------
@app.route("/attack/<mode>")
def attack(mode):

    if mode == "insider":
        subprocess.run(["python", "../core/simulate_attack.py"], input="1\n", text=True)

    elif mode == "burst":
        subprocess.run(["python", "../core/simulate_attack.py"], input="2\n", text=True)

    elif mode == "phishing":
        subprocess.run(["python", "../core/simulate_attack.py"], input="3\n", text=True)
        subprocess.run(["python", "../core/url_analyzer.py"])

    subprocess.run(["python", "../core/soc_detector.py"])

    return redirect(url_for("home"))


# ---------------- LIVE API ----------------
@app.route("/live-data")
def live_data():
    path = os.path.join(BASE_DIR, "data", "live_activity.txt")

    alerts = []

    if os.path.exists(path):
        with open(path) as f:
            lines = f.readlines()[-10:]

        for line in lines:
            line = line.strip()

            if "failed" in line.lower():
                alerts.append(f"HIGH | Failed Activity | {line}")
            elif "admin" in line.lower():
                alerts.append(f"CRITICAL | Privileged Access | {line}")
            else:
                alerts.append(f"INFO | {line}")

    return {"alerts": alerts}

if __name__ == "__main__":
    app.run(debug=True)