import os

print("Cyber SentinelX – Adaptive Threat Monitoring Platform")
print("URL Analysis Module\n")

def analyze():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, "data", "urls.txt")
    urls = open(path).readlines() if os.path.exists(path) else []

    for url in urls:
        url = url.strip()
        score = 0

        if "login" in url: score += 40
        if "secure" in url: score += 30
        if "verify" in url: score += 30

        if score >= 60:
            print(url, "→ HIGH RISK")
        elif score >= 30:
            print(url, "→ MEDIUM RISK")
        else:
            print(url, "→ LOW RISK")

if __name__ == "__main__":
    analyze()