# 08 - Django Authentication

This mini project demonstrates Django’s built-in authentication system — allowing users to log in, log out, and access protected views like a dashboard.

---

## 🚀 Features Implemented

- Login form using Django’s built-in `AuthenticationForm`
- Session management using `authenticate()`, `login()`, and `logout()`
- Protected dashboard route using `@login_required`
- User feedback via Django's messaging framework
- Redirect logic using `LOGIN_URL` and `LOGIN_REDIRECT_URL` settings

---

## 🧠 What We Learned

### 🔐 Authentication Basics
- How Django handles user login and logout under the hood
- The difference between `authenticate()` (validates) and `login()` (logs in)

### 🛡️ Access Control
- How to restrict pages using `@login_required`
- How Django redirects unauthorized users to the login page

### 🧾 Forms and Sessions
- Using Django’s built-in `AuthenticationForm` instead of writing our own
- How session cookies identify logged-in users

### 📢 User Experience
- Using Django’s `messages` framework for feedback like:
  - “Logged in successfully”
  - “Invalid credentials”
  - “You’ve been logged out”

---

## 🏁 How to Run This Project

1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

2. Install Django:
   ```
   pip install django
   ```

3. Run migrations and start the server:
   ```
   python manage.py migrate
   python manage.py runserver
   ```

4. Visit:
   - `/login/` → Log in using admin credentials
   - `/dashboard/` → Protected view
   - `/logout/` → Ends session

---

## 💡 Real-World Analogy

Imagine a club with a guest list, a bouncer, and a hand stamp. Django’s authentication system works just like that:
- Guest list → user DB
- Bouncer → `authenticate()` + `login()`
- Hand stamp → session
- VIP lounge → protected route
