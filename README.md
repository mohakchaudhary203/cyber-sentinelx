# 🔐 Cyber SentinelX – Adaptive Threat Monitoring Platform

## 🚀 Overview

Cyber SentinelX is a multi-language cybersecurity platform that simulates a real-world Security Operations Center (SOC).

It integrates authentication, threat detection, and real-time monitoring into a single system.

---

## 🧠 Features

* 🔐 Secure Authentication System (Java + SHA-256)
* 📊 SOC Detection Engine (Python)
* ⚡ Real-Time Monitoring Dashboard (Flask)
* 🚨 Automated Alert Generation
* 🔄 Live Event Streaming
* 🧩 Attack Simulation (Insider, Burst, Phishing)

---

## 🏗️ Architecture

```
Login (Java / Flask)
        ↓
Log Files (users, login, failed)
        ↓
SOC Detection Engine (Python)
        ↓
Risk Score + Alerts
        ↓
Flask Dashboard (Live Monitoring)
```

---

## 🧰 Tech Stack

* Python (Flask, SOC Detection)
* Java (Authentication Module)
* HTML, CSS, JavaScript (Dashboard UI)

---

## 📁 Project Structure

```
cyber-sentinelx/
│
├── auth/                      # Java Authentication Module
│   └── LoginSystem.java
│
├── core/                      # Python Detection + Simulation
│   ├── soc_detector.py
│   ├── simulate_attack.py
│   ├── url_analyzer.py
│   └── live_monitor.py        # (if used for generating live logs)
│
├── dashboard/                 # Flask Web App
│   ├── app.py
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   └── signup.html
│   │
│   └── static/
│       ├── style.css
│       ├── script.js
│       ├── auth.css           # (if used for login UI)
│       └── auth.js            # (if used)
│
├── data/                      # Runtime Data (DO NOT PUSH)
│   ├── users.txt
│   ├── login_log.txt
│   ├── failed_log.txt
│   ├── live_activity.txt
│   └── final_report.txt
│
├── docs/                      # (NEW 🔥 for professionalism)
│   ├── architecture.png       # optional diagram
│   └── screenshots/           # dashboard screenshots
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt 

```

---

## ▶️ How to Run

### 1. Start Flask Dashboard

```bash
cd dashboard
python app.py
```

Open:
http://127.0.0.1:5000

---

### 2. Signup

Go to:
http://127.0.0.1:5000/signup

Create account.

---

### 3. Run Java Authentication

```bash
cd auth
javac LoginSystem.java
java LoginSystem
```

---

### 4. Test System

* Successful login → logged
* Failed login → triggers alerts
* Dashboard updates automatically

---

## 📊 Output

* Real-time alerts
* Risk score updates
* Threat correlation
* Live monitoring feed

---

## 💼 Use Case

* SOC Analyst training
* Threat detection simulation
* Cybersecurity project portfolio

---

## 🚀 Future Improvements

* Database integration (MySQL / MongoDB)
* API-based communication instead of files
* Role-based access control
* Cloud deployment (AWS / Azure)
* Real SIEM integration (Splunk, ELK)

---

## 👨‍💻 Author

Mohak Chaudhary

---

## ⭐ Note

This project demonstrates practical cybersecurity concepts including:

* Authentication security
* Log-based detection
* Event correlation
* Real-time monitoring
