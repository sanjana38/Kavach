from fastapi import APIRouter
from services.vt_service import check_url_virustotal

router = APIRouter(prefix="/api")

@router.get("/vt-check")
def vt_check(url: str):
    return check_url_virustotal(url)