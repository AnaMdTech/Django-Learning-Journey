# 06-django-modelforms: Book Collection

## 📚 What this Project Covers:

In this mini project, we learned how to create and manage a Django form using `ModelForm` to add and display records (books) in a database. We built a simple **Book Collection App** with the following features:

- A form for adding books (title, author, description, published date).
- A list page to display all books added.
- We used Django’s built-in features like `ModelForm`, views, and templates to create a clean and functional app.

## 🚀 Key Concepts Covered:

1. **ModelForm**: Used to automatically generate a form from a model and save data to the database.
2. **Forms Handling**: Handling form submission and validation.
3. **Template Rendering**: Rendering forms and displaying dynamic content in templates.
4. **URL Routing**: Setting up routes to handle form submissions and viewing content.

## 🛠️ Tech Stack:

- Python 3.x
- Django 5.x

## 🚀 How to Run:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/06-django-modelforms.git
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/books/add/` to add a new book.

---

## 🧠 What I Learned:

- How to use Django's `ModelForm` to automatically create forms based on models.
- How to handle form submission and save data to the database.
- How to display dynamic content using Django templates and how to route URLs.
