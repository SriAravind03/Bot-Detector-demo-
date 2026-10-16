# 🤖 Bot Detector Demo

## 📌 About the Project

Bot Detector Demo is a simple web application developed using Python and Flask to demonstrate how honeypot techniques can help identify automated bot submissions.

The application contains a web form with a hidden field. If the hidden field is filled in during submission, the application flags the submission as suspicious and returns an HTTP 403 (Access Denied) response.

## 🎯 Objectives

- Demonstrate a basic honeypot technique for bot detection.
- Identify automated-looking form submissions.
- Understand how Flask handles form submissions.
- Demonstrate basic server-side validation.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Requests library

## ✨ Features

- Simple web-based form.
- Hidden honeypot field.
- Server-side bot detection demonstration.
- HTTP 403 response for submissions that trigger the honeypot.
- Python test script to simulate a bot submission.

## 📂 Project Structure

```text
Bot-Detector-demo/
├── app.py
├── bot_test.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    └── index.html
```

## ⚙️ How It Works

1. A visitor opens the web form.
2. The form includes a hidden honeypot field named `middle_name`.
3. A submission that fills this field is flagged as suspicious.
4. The server rejects that submission with HTTP 403.
5. A submission that leaves the field empty is treated as human-like.

## 🧪 Testing

The `bot_test.py` script sends a sample HTTP POST request with the honeypot field filled in.

The expected result is an HTTP 403 response when the Flask application is running.

## ⚠️ Limitations

This project is an educational demonstration, not a complete production-grade bot detection system. Some bots can avoid honeypot fields, and legitimate users may occasionally trigger them.

## 🚀 Future Enhancements

- Add rate limiting.
- Add CAPTCHA integration.
- Implement request and IP-based monitoring.
- Create a dashboard for suspicious submissions.
- Add logging and detection statistics.

## 👨‍💻 Author

**Sri Aravind**

GitHub: [SriAravind03](https://github.com/SriAravind03)

---

⭐ If you find this project useful, consider starring the repository.
