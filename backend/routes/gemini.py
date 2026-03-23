from fastapi import APIRouter
from services.gemini_service import analyze_with_ai

router = APIRouter(prefix="/api")

@router.get("/ai-analyze")
def ai_analysis(input: str):
    return analyze_with_ai(input)