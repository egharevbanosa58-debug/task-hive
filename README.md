# Task Hive Backend 🐝

A Django REST API for managing users and tasks, built with Django Rest Framework and JWT authentication.

---

## 🚀 Features

* User Registration (Signup)
* User Login (JWT Authentication)
* Logout (Token Blacklisting)
* User Profile (View & Update)
* Secure API Endpoints
* Ready for Task Management Features

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT (Authentication)

---

## 📂 Project Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd task-hive-backend
```

---

### 2. Create virtual environment

```bash
python -m venv task-tracker-env
```

Activate it:

**Windows:**

```bash
task-tracker-env\Scripts\activate
```

**Mac/Linux:**

```bash
source task-tracker-env/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run migrations

```bash
python manage.py migrate
```

---

### 5. Start server

```bash
python manage.py runserver
```

---

## 🔐 API Endpoints

### Auth

* `POST /api/users/signup/` → Register user
* `POST /api/users/login/` → Login user
* `POST /api/users/logout/` → Logout user
* `POST /api/users/token/refresh/` → Refresh access token

---

### Profile

* `GET /api/users/me/` → Get user profile
* `PATCH /api/users/me/` → Update profile

---

## 🧠 Notes

* Uses JWT authentication (access + refresh tokens)
* Access token is required for protected routes
* Refresh token is used to generate new access tokens
* Virtual environment is excluded from the repository

---

## 📌 Future Improvements

* Task CRUD (Create, Read, Update, Delete)
* Role-based permissions (Admin / Member)
* Password reset functionality
* Deployment

---

## 👨‍💻 Author

Built by Nosa Egharevba
