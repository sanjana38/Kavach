async function loadThreats() {
    const res = await fetch("http://127.0.0.1:8000/api/threats");
    const data = await res.json();

    const table = document.getElementById("threatTable");

    data.forEach(threat => {
        const row = `<tr>
            <td>${threat.type}</td>
            <td>${threat.indicator}</td>
            <td>${threat.risk_score}</td>
        </tr>`;
        table.innerHTML += row;
    });
}
async function checkURL() {
    const url = document.getElementById("urlInput").value;

    const res = await fetch(`http://127.0.0.1:8000/api/check?url=${url}`);
    const data = await res.json();

    document.getElementById("result").innerText =
        `Risk: ${data.risk_score} | ${data.status}`;
}

loadThreats();