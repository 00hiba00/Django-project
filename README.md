# 🍋 Little Lemon Web Application – Backend (Django Project)

This repository contains the backend implementation for the Little Lemon Web Application, built with Django, Django REST Framework (DRF), and Djoser for token-based authentication.
The project uses SQLite as the database and exposes APIs for menu management, reservations, and user management.

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.2-green?logo=django)](https://www.djangoproject.com/)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/00hiba00/Django-project)

Table of Contents
- [About](#about)
- [Project Overview](#project-overview)
- [Project structure](#project-structure)
- [Quickstart](#quickstart)
- [URL Endpoints & Usage](#url-endpoints-usage)
- [Running Unit Tests](#running-unit-tests)

## 📖 About
**Problem this project solves:**  
Restaurants often struggle with managing menu items, tracking reservations, and handling user accounts efficiently. Manual management can lead to errors, double bookings, and slow service.  

**Target audience:**  
- Small restaurants or cafes needing a digital backend  
- Developers or teams building a restaurant web application  
- Students learning Django, REST APIs, and token-based authentication  

**High-level approach:**  
- Built with **Django** as the main web framework  
- Uses **Django REST Framework** for RESTful APIs  
- **Djoser** provides token-based authentication for secure access  
- **SQLite** database stores menu items, reservations, and users  
- Exposes APIs for menu management, reservations, and users, plus a simple homepage and admin panel  

## 📌 Project Overview

- Homepage (`index.html`) served via Django views
- REST API endpoints:
  - **Menu items** (`/menu/`)
  - **Reservations** (`/reservation/booking/tables/`, requires token)
  - **Users** (`/users/`, requires token)
- Token-based authentication via **Djoser**
- Admin interface (`/admin/`)
- Unit tests for models and APIs
- SQLite as the database

## 🗂️Project structure
Below is a suggested/typical Django project structure. Replace the placeholders (project_name, app_name) with the actual names in your repo or let me fetch the exact tree and I'll update this.
```
Django-project/
├── manage.py
├── README.md
├── db.sqlite3
├── littlelemon/                 
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── reservation/                    
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py               
│   └── migrations/
│       └── __init__.py
│   ├── templates/
│       └── index.html
│    ├── static/
│       └── images/
│           └── logo.png
├── tests/                    
│   ├── __init__.py
│   ├── test_models.py                    
```

## 🚀 Quickstart (development)
```
1. Clone the repo
   git clone https://github.com/00hiba00/Django-project.git
   cd Django-project

2. Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate

3. Install dependencies
   pip install django djangorestframework djoser

4. Apply migrations
   python manage.py migrate

5. Create a superuser 
   python manage.py createsuperuser

6. Run the development server
   python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.
```

## 🌐 URL Endpoints & Usage

### **Home page**
- `/` → index.html

### **Menu API**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `reservation/menu/` | List all menu items |
| POST | `reservation/menu/` | Create a new menu item |
| GET | `reservation/menu/<id>/` | Retrieve a menu item |
| PUT/PATCH | `reservation/menu/<id>/` | Update a menu item |
| DELETE | `reservation/menu/<id>/` | Delete a menu item |

### **Reservation API (token required)**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/reservation/booking/tables/` | List reservations |
| POST | `/reservation/booking/tables/` | Create reservation |
| GET | `/reservation/booking/tables/<id>/` | Retrieve reservation |
| PUT/PATCH | `/reservation/booking/tables/<id>/` | Update reservation |
| DELETE | `/reservation/booking/tables/<id>/` | Delete reservation |

### **User API (token required)**
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/` | List all users |

### **Authentication (Djoser)**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/token/login/` | Log in and get token |
| POST | `/auth/token/logout/` | Log out |
| POST | `/auth/users/` | Register user |
| GET | `/auth/users/me/` | Get current user info |

**Example — using token to access bookings:**

```bash
curl -H "Authorization: Token YOUR_TOKEN_HERE" \
http://127.0.0.1:8000/reservation/booking/tables/
```

### **Admin**
`/admin/` : Django admin panel

## 🧪 Running Unit Tests
python manage.py test

