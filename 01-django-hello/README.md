# 01 - Django Hello 🌍

This is the first mini project of the Django Learning Journey. It focuses on setting up a basic Django project and app, and rendering a simple "Hello, Django World!" message in the browser.

---

## 🎯 What This Project Covers

- Installing Django
- Creating a new project and app
- Understanding the project structure
- Writing your first view
- Mapping views to URLs
- Running the development server

---

## 📁 File Breakdown

| File | Purpose |
|------|---------|
| `manage.py` | Django’s command-line utility |
| `django_hello/settings.py` | Project settings (apps, middleware, templates, etc.) |
| `main/views.py` | Where we wrote our "Hello, Django World!" view |
| `main/urls.py` | URL routing specific to the `main` app |
| `django_hello/urls.py` | Project-wide routing entry point |

---

## 🚀 Steps to Run

1. Navigate to this folder
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install Django
   ```bash
   pip install django
   ```
4. Run the server
   ```bash
   python manage.py runserver
   ```
5. Visit `http://127.0.0.1:8000/` in your browser

---

## 💡 What I Learned

- How to bootstrap a Django project from scratch
- The difference between a **project** and an **app**
- How routing works in Django
- How to return a basic HTTP response

---

## ✅ Practice Ideas

- Add another URL route (like `/about`) with a different message
- Try returning some basic HTML inside the response
- Play around with the port (`python manage.py runserver 8080`)

## 🤝 Contribute

Feel free to fork, clone, or PR this project to improve it or use it as a base for your own learning!