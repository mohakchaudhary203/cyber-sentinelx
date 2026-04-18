function runAttack(type) {
    document.body.style.cursor = "wait";
    window.location.href = "/attack/" + type;
}

// 🔥 LIVE DATA FETCH
function loadLiveData() {
    fetch("/live-data")
        .then(res => res.json())
        .then(data => {
            const box = document.getElementById("liveBox");
            box.innerHTML = "";

            data.alerts.forEach(a => {
                const div = document.createElement("div");
                div.className = "alert";

                // 🔥 Severity tagging
                if (a.toLowerCase().includes("failed")) {
                    div.classList.add("high");
                } else if (a.toLowerCase().includes("privileged")) {
                    div.classList.add("critical");
                } else {
                    div.classList.add("info");
                }

                // 🔥 Timestamp
                const time = new Date().toLocaleTimeString();
                div.innerText = `[${time}] ${a}`;

                box.appendChild(div);
            });

            // 🔥 Auto-scroll
            box.scrollTop = box.scrollHeight;
        })
        .catch(() => {
            console.log("Live data fetch failed");
        });
}

// 🔥 STATUS GLOW
function highlightStatus() {
    const statusBox = document.querySelector(".box:last-child");

    if (!statusBox) return;

    const text = statusBox.innerText.toLowerCase();

    if (text.includes("critical")) {
        statusBox.style.boxShadow = "0 0 20px red";
    } else if (text.includes("warning")) {
        statusBox.style.boxShadow = "0 0 20px orange";
    } else {
        statusBox.style.boxShadow = "0 0 20px green";
    }
}

// 🔁 AUTO REFRESH
setInterval(loadLiveData, 2000);

window.onload = function () {
    loadLiveData();
    highlightStatus();
};