import requests
from config import URLSCAN_API_KEY

def scan_url(url):
    headers = {
        "API-Key": URLSCAN_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "url": url,
        "visibility": "public"
    }

    try:
        # Step 1: Submit scan
        res = requests.post(
            "https://urlscan.io/api/v1/scan/",
            headers=headers,
            json=data
        )

        if res.status_code != 200:
            return {"error": "Scan submission failed"}

        scan_result = res.json()
        result_url = scan_result.get("result")

        return {
            "source": "urlscan",
            "scan_link": result_url
        }

    except Exception as e:
        return {"error": str(e)}