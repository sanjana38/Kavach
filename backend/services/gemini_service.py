import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1")

def analyze_with_ai(input_text):
    prompt = f"""
    Analyze the following input for cyber threats, phishing, or scams.

    Input: {input_text}

    Give:
    - Risk level (Safe / Suspicious / High Risk)
    - Reason
    - If it's a scam or phishing

    Keep it short and clear.
    """

    try:
        response = model.generate_content(prompt)

        return {
            "source": "Gemini AI",
            "analysis": response.text
        }

    except Exception as e:
        return {"error": str(e)}