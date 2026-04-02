console.log("Frontend ready");

// Dashboard
fetch("http://127.0.0.1:8000/sensors/latest")
    .then(res => res.json())
    .then(data => {
        document.getElementById("temp-value").textContent = data.temperature + " °C";
        document.getElementById("humidity-value").textContent = data.humidity + " %";
        document.getElementById("light-value").textContent = data.light + " lx";
    });

// Historique
fetch("http://127.0.0.1:8000/sensors/history")
    .then(res => res.json())
    .then(data => {
        const table = document.getElementById("history-table");
        table.innerHTML = "";

        data.items.forEach(row => {
            table.innerHTML += `
                <tr>
                    <td class="border p-2">${row.timestamp}</td>
                    <td class="border p-2">${row.sensor}</td>
                    <td class="border p-2">${row.value}</td>
                </tr>
            `;
        });
    });

// Alertes
fetch("http://127.0.0.1:8000/alerts/")
    .then(res => res.json())
    .then(alerts => {
        const list = document.getElementById("alerts-list");
        list.innerHTML = "";

        if (alerts.length === 0) {
            list.innerHTML = `<li class="p-4 bg-green-100 border border-green-300 rounded">Aucune alerte.</li>`;
            return;
        }

        alerts.forEach(a => {
            list.innerHTML += `
                <li class="p-4 bg-red-100 border border-red-300 rounded">
                    <strong>${a.type.toUpperCase()}</strong> — ${a.message} (${a.value})
                </li>
            `;
        });
    });
