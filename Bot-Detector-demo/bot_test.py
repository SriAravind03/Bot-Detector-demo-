import requests

URL = "http://127.0.0.1:5000/submit"

# Deliberately fill the honeypot field to exercise the detector.
bot_data = {
    "username": "Terminator_Bot",
    "middle_name": "I am a robot filling your hidden trap!",
}

print("--- Sending Bot Submission ---")
try:
    response = requests.post(URL, data=bot_data, timeout=10)
    if response.status_code == 403:
        print("RESULT: Success! The honeypot blocked the submission (HTTP 403).")
    else:
        print(f"RESULT: Unexpected response: HTTP {response.status_code}")
        print(response.text)
except requests.RequestException as exc:
    print(f"Could not reach the Flask app at {URL}: {exc}")
