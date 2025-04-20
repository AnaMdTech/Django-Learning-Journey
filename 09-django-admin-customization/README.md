# 09-django-admin-customization

This project demonstrates how to customize the Django admin panel using the **AdminLTE** theme, along with **django-admin-interface** for an enhanced look and feel.

## Overview

The project focuses on integrating AdminLTE, a popular open-source admin dashboard template, with Django's built-in admin panel. The `django-admin-interface` package is used to further enhance the look and behavior of the admin interface. This customization provides a clean, modern, and user-friendly interface for administrative tasks.

### Features:
- Integration of the AdminLTE theme with Django admin.
- Installation of `django-admin-interface` for better customization options.
- Basic setup to get started with Django admin customizations.

## Setup Instructions

### Step 1: Set up a new Django project

```bash
django-admin startproject django_admin_customization
cd django_admin_customization
```

### Step 2: Install dependencies

In your virtual environment, install Django and the required packages:

```bash
pip install django django-admin-interface
```

### Step 3: Update `INSTALLED_APPS`

Add `'admin_interface'`, `'colorfield'`, and `'django.contrib.admin'` to the `INSTALLED_APPS` section in your `settings.py` file.

```python
INSTALLED_APPS = [
    ...
    'django.contrib.admin',
    'admin_interface',
    'colorfield',
]
```

### Step 4: Apply migrations

Run the following command to apply any migrations required for `django-admin-interface`:

```bash
python manage.py migrate
```

### Step 5: Configure the Admin Interface

Create a custom admin interface by using AdminLTE’s HTML and CSS. Use `admin_interface` to customize colors and other settings.

### Step 6: Create and load a superuser

Create a superuser to log in to the admin interface:

```bash
python manage.py createsuperuser
```

### Step 7: Run the server

Finally, run the development server:

```bash
python manage.py runserver
```

You can now log in to the Django admin panel using the superuser account and see the AdminLTE theme applied.