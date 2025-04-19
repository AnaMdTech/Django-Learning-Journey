# 📬 05-django-forms

This mini project demonstrates how to use **Django forms** to create and process a basic contact form.

---

## 🚀 What We Learned

- How to use Django’s `forms.Form` class to create a form in Python
- Rendering forms in HTML templates using `{{ form.as_p }}`
- Handling form submission in views using `request.POST`
- Showing a success message after the form is submitted
- Using CSRF protection in Django templates
- Structuring templates and using app-level directories

---

## 🧪 Real-World Use Cases

This technique is foundational for building:

- Contact pages
- Feedback forms
- Newsletter signups
- Job applications
- Any user input form that doesn’t require a model

---

## 📂 Folder Structure

```
05-django-forms/
├── contact/
│   ├── templates/
│   │   └── contact/
│   │       └── contact.html
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
├── django_forms/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── venv/
```

---

## ▶️ How to Run

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. Run the server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser:
   [http://127.0.0.1:8000/contact/](http://127.0.0.1:8000/contact/)

---

## 🧠 Final Thoughts

Django forms are a great way to handle user input cleanly and securely. They're built to scale with your project — from simple forms to advanced ones tied to models and databases (coming next!).
