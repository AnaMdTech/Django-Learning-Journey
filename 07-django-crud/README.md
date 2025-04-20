# 🗂️ 07-django-crud

This mini project demonstrates how to implement **CRUD (Create, Read, Update, Delete)** operations in Django using a simple task manager app.

---

## 📚 What This Project Covers

- How to define a model (`Task`) in Django
- Using `ModelForm` to create and update data
- Rendering and handling forms in templates
- Displaying records using views
- Updating existing records via pre-filled forms
- Deleting records safely with a confirmation step
- Using Django messages to show success notifications

---

## 🛠 Features Built

| Functionality | Description |
|---------------|-------------|
| **Create**    | Add a new task using a form |
| **Read**      | View a list of all tasks |
| **Update**    | Edit an existing task (e.g. change title or mark as complete) |
| **Delete**    | Remove a task with confirmation |

---

## 🧠 What I Learned

- CRUD operations are the backbone of most web applications.
- Django makes CRUD much easier with `ModelForm` and class-based or function-based views.
- Handling forms properly includes validation, instance tracking, and redirecting after submission.
- Showing feedback messages with `django.contrib.messages` improves UX.
- Using template logic (e.g., `{% if task.completed %}`) helps with conditional UI rendering.

---

## 🖼 Example UI

- Task form: Add or edit a task
- Task list: Shows all tasks with edit/delete buttons
- Confirmation screen: Before deleting a task

---

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd 07-django-crud
   ```

2. Create & activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## ✅ Status

✔️ CRUD features implemented  
✔️ Functional and easy to extend  
✔️ Styled with minimal CSS for readability