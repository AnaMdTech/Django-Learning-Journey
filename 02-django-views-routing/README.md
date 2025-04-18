# 🚀 02-django-views-routing

This mini project demonstrates how to use **Django Views**, **URL patterns**, and **dynamic routing** — the foundation for building web pages and handling requests in real-world Django applications.

---

## 📚 What This Covers

- ✅ How to create **view functions** in Django
- ✅ How to set up **static URL routes**
- ✅ How to use **dynamic URL parameters** (e.g., passing a username via URL)
- ✅ How to connect app-level and project-level URL configurations

---

## 🛠️ What We Built

| URL | Description |
|-----|-------------|
| `/` | Returns a "Welcome" message |
| `/about/` | Displays a static About message |
| `/hello/<name>/` | Greets the user by name (dynamic route) |

Example:
- Visiting `/hello/ana/` shows `Hello, Ana! 👋🏾`

---

## 🧠 What You’ll Learn

This project helps you understand:
- The role of `views.py` in returning web responses
- How to create readable and clean URL patterns
- How to pass variables from the URL into your view function
- Real-world application: user profiles, blog posts, product pages, etc.

---

## 📁 Project Structure

```
02-django-views-routing/
├── django_views_routing/        # Project settings & URLs
│   └── urls.py                  # Project-level URL routing
├── main/                        # App containing views
│   ├── views.py                 # Home, about, and greet views
│   └── urls.py                  # App-level routing
├── venv/                        # Virtual environment
├── manage.py
└── README.md
```

---

## ▶️ How to Run

1. Activate virtual environment:
    ```bash
    source venv/bin/activate     # Mac/Linux
    venv\Scripts\activate        # Windows
    ```

2. Run the server:
    ```bash
    python manage.py runserver
    ```

3. Open in browser:
    - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Try `/hello/yourname/`

---

## 💡 Try This Next

- Add another dynamic route: `/profile/<username>/`
- Use `<int:id>` in a URL pattern
- Return HTML templates instead of raw strings

---

## 🤝 Contribute

Feel free to fork, clone, or PR this project to improve it or use it as a base for your own learning!