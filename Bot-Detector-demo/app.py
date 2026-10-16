from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    # A honeypot field should remain empty for normal users.
    honeypot = request.form.get("middle_name", "").strip()
    if honeypot:
        app.logger.warning("Bot-like submission blocked by honeypot.")
        return (
            "<h1>Access Denied</h1>"
            "<p>Automated-looking submission detected.</p>",
            403,
        )

    # Escape user-controlled text before including it in the response HTML.
    username = escape(request.form.get("username", "").strip() or "visitor")
    return (
        f"<h1>Success!</h1><p>Welcome, {username}. "
        "This demo treated the submission as human.</p>"
    )


if __name__ == "__main__":
    # Debug mode is disabled unless explicitly enabled for local development.
    import os

    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
