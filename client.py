import requests

from config import API_KEY, MODEL
from persona import SYSTEM_PROMPT

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


def ask_neuro(user_message: str) -> str:
    """Send one user message to Gemini (as Neuro) and return the reply text."""
    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [{"role": "user", "parts": [{"text": user_message}]}],
    }
    response = requests.post(URL, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]
