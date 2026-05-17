// =======================
// CHART
// =======================

const ctx = document.getElementById('vulnChart');

new Chart(ctx, {

    type: 'bar',

    data: {

        labels: [
            'SQL Injection',
            'XSS',
            'CSRF',
            'SSRF',
            'Open Redirect'
        ],

        datasets: [{

            label: 'Detected Vulnerabilities',

            data: [12, 19, 7, 5, 9],

            backgroundColor: [
                '#8b5cf6',
                '#06b6d4',
                '#f59e0b',
                '#ef4444',
                '#10b981'
            ],

            borderRadius: 8
        }]
    },

    options: {

        responsive: true,

        plugins: {

            legend: {
                labels: {
                    color: 'white'
                }
            }
        },

        scales: {

            x: {

                ticks: {
                    color: 'white'
                },

                grid: {
                    color: '#1f2937'
                }
            },

            y: {

                ticks: {
                    color: 'white'
                },

                grid: {
                    color: '#1f2937'
                }
            }
        }
    }
});


// =======================
// LIVE SCAN FUNCTION
// =======================

async function startScan() {

    const target = document.getElementById("targetInput").value;

    const terminal = document.getElementById("terminal");

    const tableBody = document.getElementById("urlTableBody");

    const findingsBody = document.getElementById("findingsTableBody");

    // Clear previous results

    tableBody.innerHTML = "";

    findingsBody.innerHTML = "";

    terminal.innerHTML = "";

    // Logs

    addLog("[INFO] Initializing scanner...");
    addLog("[INFO] Target: " + target);
    addLog("[INFO] Crawling started...");

    try {

        const response = await fetch("/scan", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                target: target
            })
        });

        const data = await response.json();

        addLog("[SUCCESS] Crawling completed.");

        // =======================
        // URLs
        // =======================

        if(data.urls.length > 0){

            data.urls.forEach((url, index) => {

               const tr = document.createElement("tr");

const td1 = document.createElement("td");
td1.textContent = index + 1;

const td2 = document.createElement("td");
td2.textContent = url;

tr.appendChild(td1);
tr.appendChild(td2);

tableBody.appendChild(tr);
                addLog("[FOUND] " + url);

            });

        } else {

            tableBody.innerHTML = `
                <tr>
                    <td colspan="2">
                        No URLs found.
                    </td>
                </tr>
            `;

            addLog("[WARNING] No URLs found.");
        }

        // =======================
        // Findings
        // =======================

        if(data.findings.length > 0){

            data.findings.forEach((finding) => {

                const severityClass =
                    finding.severity === "Critical"
                    ? "bg-danger"
                    : "bg-warning";

                const tr = document.createElement("tr");

const td1 = document.createElement("td");
td1.textContent = finding.url;

const td2 = document.createElement("td");
td2.textContent = finding.type;

const td3 = document.createElement("td");

const badge = document.createElement("span");

badge.className = `badge ${severityClass}`;

badge.textContent = finding.severity;

td3.appendChild(badge);

const td4 = document.createElement("td");
td4.textContent = "Detected";

tr.appendChild(td1);
tr.appendChild(td2);
tr.appendChild(td3);
tr.appendChild(td4);

findingsBody.appendChild(tr);

                addLog(
                    "[VULNERABLE] " +
                    finding.type +
                    " detected."
                );

            });

        } else {

            findingsBody.innerHTML = `
                <tr>
                    <td colspan="4">
                        No vulnerabilities found.
                    </td>
                </tr>
            `;

            addLog("[INFO] No vulnerabilities detected.");
        }

    } catch(error){

        addLog("[ERROR] Scan failed.");

        console.log(error);
    }
}


// =======================
// TERMINAL LOG FUNCTION
// =======================

function addLog(message){

    const terminal = document.getElementById("terminal");

    const p = document.createElement("p");

    p.textContent = message;

    terminal.appendChild(p);

    terminal.scrollTop = terminal.scrollHeight;
}