# Bot Detector Demo

A minimal Flask app that demonstrates a honeypot field for identifying automated-looking form submissions.

## Files

- `app.py` — Flask server and `/submit` honeypot check.
- `templates/index.html` — form with a visually hidden honeypot input.
- `bot_test.py` — sends a test submission that fills the honeypot field.
- `requirements.txt` — Python dependencies.

## Run locally

Requires Python 3.10 or newer.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

In a second terminal with the virtual environment activated, run:

```powershell
python bot_test.py
```

The test script should receive HTTP 403 when the honeypot field is filled.

## Limitations

This is an educational demonstration, not a production anti-bot system. Legitimate users can trigger honeypots, and sophisticated bots may avoid them. Production forms should also use robust server-side validation, rate limiting, CSRF protection where applicable, and appropriate monitoring. Flask debug mode is off by default.

## Upload to your GitHub repository (Windows PowerShell)

After extracting this folder, open it in VS Code and use Terminal → New Terminal. Run these commands from the project folder. The target repository is currently empty.

```powershell
git init -b main
git add .
git commit -m "Add Bot Detector Flask demo"
git remote add origin https://github.com/SriAravind03/Bot-Detector-demo-.git
git push -u origin main
```

If Git asks you to sign in, complete the browser/Git Credential Manager sign-in. Do not put a GitHub password or access token in the command.
