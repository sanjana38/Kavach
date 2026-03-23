import requests
import base64
from config import VIRUSTOTAL_API_KEY

headers = {
    "x-apikey": VIRUSTOTAL_API_KEY
}

# Step 1: Submit URL
def submit_url(url):
    response = requests.post(
        "https://www.virustotal.com/api/v3/urls",
        headers=headers,
        data={"url": url}
    )
    return response.json()

# Step 2: Get report
def get_report(url):
    encoded_url = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

    response = requests.get(
        f"https://www.virustotal.com/api/v3/urls/{encoded_url}",
        headers=headers
    )
    return response.json()

# Final function
def check_url_virustotal(url):
    submit_url(url)  # 🔥 important step

    data = get_report(url)

    try:
        stats = data["data"]["attributes"]["last_analysis_stats"]

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)

        score = malicious * 20 + suspicious * 10

        return {
            "source": "VirusTotal",
            "malicious": malicious,
            "suspicious": suspicious,
            "risk_score": score
        }

    except:
        return {"error": "No analysis yet"}