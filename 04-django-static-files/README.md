# 📁 04-django-static-files

This mini project demonstrates how to **work with static files in Django**, such as CSS and images. It's a foundational skill needed for styling real-world Django applications.

---

## ✅ What We Covered

- How to set up and organize static files in Django
- Linking external CSS using the `{% static %}` template tag
- Loading and applying custom styles to templates
- Creating and using a `base.html` layout with `{% extends %}`
- Rendering multiple views (`home`, `about`) with shared styling

---

## 🧠 What You Learned

- Why static files are important for real-world apps (styling, images, JS)
- How Django looks for static files via `STATICFILES_DIRS`
- How to use `{% load static %}` and `{% static 'path/to/file.css' %}` in templates
- How to keep your project clean by separating static and template files

---

## 📁 Folder Structure

```
04-django-static-files/
├── main/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── about.html
│   └── views.py
├── django_static/
│   └── settings.py (with STATICFILES_DIRS configured)
├── manage.py
├── README.md
```

---

## 🚀 Run This Project

1. Activate the virtual environment
   ```bash
   venv\Scripts\activate  # or source venv/bin/activate
   ```

2. Run the development server
   ```bash
   python manage.py runserver
   ```

3. Visit the pages:
   - Home: http://127.0.0.1:8000/
   - About: http://127.0.0.1:8000/about/

---

## 💡 Real World Use Cases

- Using CSS frameworks like Tailwind or Bootstrap
- Adding user-uploaded images or branding assets
- Creating JavaScript-powered features with static JS

---

## 📘 Next Steps

In upcoming projects, we’ll work with:
- Template inheritance & layout strategies
- Static images & favicon
- Custom JS files for interactivity