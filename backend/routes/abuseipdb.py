from fastapi import APIRouter
from services.abuse_service import check_ip_abuse

router = APIRouter(prefix="/api")

@router.get("/ip-check")
def ip_check(ip: str):
    return check_ip_abuse(ip)