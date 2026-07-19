<div align="center">
  <img src="./banner.png" width="140" height="140" style="border-radius:50%; object-fit:cover;" alt="NeuroFive Solutions"/>
# Neuro — Neurofive Solutions Support Bot

A small multi-file demo of calling the Gemini API with a custom system
prompt to create a persona: **Neuro**, support assistant for a fictional
company, Neurofive Solutions.

## File structure
| File | Purpose |
|---|---|
| `config.py` | Loads your API key and sets the model name |
| `persona.py` | The system prompt — Neuro's personality and rules |
| `client.py` | The function that actually calls the Gemini API |
| `test_messages.py` | The 5 test messages |
| `main.py` | Runs everything — **this is the file you execute** |
| `server.py` | Flask backend for the browser chat UI |
| `templates/index.html` | The chat UI itself (HTML/CSS/JS, no build step) |
| `.env.example` | Template showing what your `.env` file should look like |
| `requirements.txt` | Python packages needed |

## Setup (in VS Code)
1. Open this folder (`neuro-bot`) in VS Code.
2. Open a terminal: **Terminal → New Terminal**.
3. (Optional but recommended) create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Get a free-tier API key (no credit card needed) at
   https://aistudio.google.com — sign in with a Google account, then
   click "Get API key" → "Create API key".
6. Copy `.env.example` to a new file named `.env`, then paste your real
   key in:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` so it reads:
   ```
   GEMINI_API_KEY=your-real-key
   ```
7. Run it:
   ```bash
   python main.py
   ```

You should see all 5 test messages printed along with Neuro's replies.

## Web chat UI
For a real browser-based chat window instead of terminal output:
```bash
python server.py
```
Then open http://127.0.0.1:5000 in your browser. `server.py` and
`templates/index.html` reuse the same `config.py` and `persona.py` —
Neuro's rules and API key are identical to the terminal version.

## Why split into files like this?
- `persona.py` is the only file you'd touch to build a completely
  different bot (study buddy, IT helpdesk, etc.).
- `client.py` isolates the actual API call — swapping to OpenAI or
  Claude later means only editing this one file.
- `test_messages.py` keeps your test cases easy to find and extend.
- `main.py` stays tiny and readable since it just wires the pieces
  together.

## Sharing your work
Push the whole `neuro-bot` folder to a public GitHub repo (the `.env`
file will be excluded automatically thanks to `.gitignore` — **never
commit your real API key**):
```bash
git init
git add .
git commit -m "Neurofive support bot demo"
git remote add origin <your-repo-url>
git push -u origin main
```
