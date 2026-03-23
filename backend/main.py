from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json
import ipaddress
import os
from routes.vt import router as vt_router
from routes.abuseipdb import router as abuse_router
from routes.urlscan import router as urlscan_router
from routes.gemini import router as gemini_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data
with open("threats.json") as f:
    threats = json.load(f)

# Home
@app.get("/")
def home():
    return {"message": "CTI Platform Running"}

# Get threats
@app.get("/api/threats")
def get_threats():
    return threats

# Check URL / IP
@app.get("/api/check")
def check_url(url: str):
    score = 0

    # Check IP
    try:
        ip = ipaddress.ip_address(url)
        if ip.is_private:
            return {
                "url": url,
                "risk_score": 0,
                "status": "Private IP (Internal Network)"
            }
    except:
        pass

    # Rules
    if "login" in url:
        score += 40
    if "free" in url:
        score += 20
    if ".xyz" in url:
        score += 30
    if "upi" in url.lower():
        score += 30
    if "pay" in url.lower():
        score += 20

    status = "Safe" if score < 50 else "Suspicious"

    return {
        "url": url,
        "risk_score": score,
        "status": status
    }

app.include_router(vt_router)
app.include_router(abuse_router)
app.include_router(urlscan_router)
app.include_router(gemini_router)


# Serve frontend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
frontend_path = os.path.join(BASE_DIR, "..", "frontend")

app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")