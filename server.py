"""
server.py

Flask backend for the Neuro web chat UI. Wraps the same Gemini call
used by client.py, but supports multi-turn conversation history so
the browser gets a real back-and-forth chat instead of one-off replies.

Run with:
    pip install flask
    python server.py
Then open http://127.0.0.1:5000 in your browser.
"""

import requests
from flask import Flask, render_template, request, jsonify

from config import API_KEY, MODEL
from persona import SYSTEM_PROMPT

app = Flask(__name__)

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = data.get("message", "")
    history = data.get("history", [])  # [{role: "user"|"assistant", text: "..."}]

    contents = []
    for turn in history:
        role = "model" if turn.get("role") == "assistant" else "user"
        contents.append({"role": role, "parts": [{"text": turn.get("text", "")}]})
    contents.append({"role": "user", "parts": [{"text": user_message}]})

    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": contents,
    }

    response = requests.post(URL, json=payload, timeout=30)
    response.raise_for_status()
    reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
