# 🧩 03-django-templates

This mini project introduces one of the most important parts of Django development: **Templates**.

Templates let you build real web pages by combining **HTML + dynamic data**. They’re the visual layer of any Django app, letting you render content in a reusable, organized way.

---

## 🚀 What This Covers

- Rendering views with `render(request, template_name)`
- Creating a `templates/` folder in your app
- Using Django Template Language (DTL):
  - `{{ variable }}` for dynamic data
  - `{% block %}` and `{% extends %}` for layout inheritance
- Linking multiple pages with proper routing
- Dynamic URL data (`/greet/<name>/`) passed to templates

---

## 🧠 What We Learned

| Concept | Description |
|--------|-------------|
| `render()` | Replaces `HttpResponse` to return HTML files |
| Template Folder | Each app has its own `templates/` folder |
| `base.html` | A parent layout shared across pages |
| `{% extends %}` | Lets pages reuse a base layout |
| `{{ name }}` | Dynamically outputs content passed from view |
| Routing | How to connect paths like `/`, `/about/`, and `/greet/<name>/` |

---

## 🛠 How to Run This Project

```bash
cd 03-django-templates
python -m venv venv
venv\Scripts\activate     # or source venv/bin/activate (Mac/Linux)
pip install django
python manage.py runserver
```

Then open your browser and try:

- `/` – Homepage
- `/about/` – About page
- `/greet/ana/` – Dynamic page that greets Ana (or any name)

---

## 💡 Real-World Application

In real apps, templates are used to:
- Render blog posts, product listings, user profiles
- Share layout (like header, footer, navigation)
- Show dynamic content fetched from databases

---

## ✅ Project Summary

We’ve now learned how to make Django pages feel like real web apps — with structure, visuals, and dynamic data. Templates are a huge part of the Django workflow, and we’ll keep building on this in future projects.