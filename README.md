# 🍎 Fruit Project (Django → JSON → Frontend Test)

## 🧩 Project Description
This repository is **for learning and testing purposes only**.  
The main goal is to demonstrate **a simple JSON communication flow between a Django backend and a separate frontend**.

The setup is intentionally minimal:
- The **backend (Django)** provides a JSON response (e.g., a list of fruits).
- The **frontend (HTML + JS)** fetches this JSON data and displays it in the browser.

---

## 📁 Project Structure
```
fruit_project/
│
├── core/                # Django project configuration (Settings, URLs, WSGI)
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── fruit_app/           # Django app providing JSON via views
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
│
├── fruit_frontend/      # Simple frontend (outside of Django templates)
│   ├── index.html       # Basic HTML page
│   └── script.js        # Fetches JSON from backend using Fetch API
│
├── db.sqlite3           # Local SQLite database
├── manage.py            # Django CLI
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Activate Virtual Environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows PowerShell
# or
source .venv/bin/activate      # macOS/Linux
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Django Server
```bash
python manage.py runserver
```
The server runs by default at:  
`http://127.0.0.1:8000/`

---

## 🌐 Frontend Access
The frontend is **completely separate from Django** — open it directly via your browser:
```
fruit_frontend/index.html
```

`script.js` will then use the `fetch()` API to get JSON data from the Django backend.

---

## 🧠 Learning Goals
This project demonstrates how to:
- create a simple JSON API with Django,
- connect a static frontend to a Django backend,
- test and visualize the communication between both sides.

---

## ⚠️ Disclaimer
This is **not a production-ready project**.  
It is designed **solely for educational, testing, and learning purposes**, focusing on:
- Django basics
- JSON data handling
- Fetch API usage

---

## 👨‍💻 Author
**Abbas El Mahmoud**  
_Test project – for educational purposes only_
