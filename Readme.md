# WTD Backend (Django + PostgreSQL)

This repository contains the backend system for **WTD (World Trade Developers)** — a large-scale event, exhibition, and matchmaking platform.

The backend is built using **Django + Django Rest Framework**, with **PostgreSQL** as the primary database and **Flutter** as the mobile client.

---

## 🚀 Project Overview

WTD is a comprehensive platform designed to manage:

* International trade events
* Exhibitors and booths
* Attendees and ticketing (QR-based)
* Business matchmaking and meetings
* CMS-driven website & mobile app content
* Payments and analytics

The backend exposes secure REST APIs consumed by:

* Flutter mobile app
* Admin/CMS dashboard
* Public website

---

## 🏗️ Architecture Overview

This project follows a **feature-based modular architecture**.

```
wtd_project/
├─ wtd_project/        # Project settings, URLs, ASGI/WSGI
├─ apps/               # Feature-based Django apps
│  ├─ users/           # Authentication, roles, profiles
│  ├─ events/          # Events, sessions, speakers
│  ├─ exhibitors/      # Companies, booths, products
│  ├─ tickets/         # Ticketing, QR codes, check-ins
│  ├─ matchmaking/     # Business matching & meetings
│  ├─ cms/             # Pages, news, downloads
│  ├─ payments/        # Payment gateway integration
│  ├─ notifications/   # Email & push notifications
│  ├─ adminpanel/      # Custom admin utilities (optional)
│  └─ analytics/       # Reports, exports, dashboards
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
└─ README.md
```

Each app follows **separation of concerns**:

* `models.py` → database schema
* `views.py` → API controllers
* `serializers.py` → request/response validation
* `services.py` → business logic
* `repositories.py` → database queries (optional)

---

## 🧠 Key Concepts

### 1. Custom User Model

* Email-based authentication
* UUID primary keys
* Role-based access (`attendee`, `exhibitor`, `organizer`, `admin`)
* Optional company (exhibitor) linkage

### 2. Ticketing & QR System

* Each ticket has a unique QR token
* QR scanned at event check-in
* Prevents duplicate entry using atomic DB operations

### 3. Matchmaking System

* Attendees & exhibitors create match profiles
* Send and accept meeting requests
* Schedule meetings within event timeline

### 4. CMS (Content Management System)

* Admins manage pages, news, downloads, media
* Content served dynamically to website & app
* No redeployment required for content changes

---

## 🛠️ Tech Stack

**Backend**

* Python 3.10+
* Django 4+
* Django Rest Framework
* PostgreSQL

**Mobile App**

* Flutter

**Other Tools**

* Docker & Docker Compose
* JWT Authentication
* Stripe (Payments)
* Celery & Redis (Async tasks – optional)

---

## ⚙️ Local Setup Instructions

### 1. Clone the repository

```
git clone <repository-url>
cd wtd_project
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment v
