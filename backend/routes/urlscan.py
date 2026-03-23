from fastapi import APIRouter
from services.urlscan_service import scan_url

router = APIRouter(prefix="/api")

@router.get("/urlscan")
def urlscan_check(url: str):
    """
    Scan a URL using urlscan.io
    """
    result = scan_url(url)

    return {
        "input": url,
        "urlscan": result
    }