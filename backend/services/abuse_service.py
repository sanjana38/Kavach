import requests
from config import ABUSEIPDB_API_KEY

def check_ip_abuse(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            return {"error": "API error"}

        data = response.json()["data"]

        score = data.get("abuseConfidenceScore", 0)

        return {
            "source": "AbuseIPDB",
            "ip": ip,
            "abuse_score": score,
            "isp": data.get("isp"),
            "country": data.get("countryCode"),
            "risk_score": score  # direct mapping
        }

    except Exception as e:
        return {"error": str(e)}