# Django Project Template

A Django project template following Django conventions with a clean, modular architecture featuring views, URLs, models, and services.

## Project Structure

```
.
├── app.py                 # Main application entry point (optional Flask-like interface)
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── config/               # Django project configuration
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration (root URLs)
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── apps/                 # Django application
│   ├── __init__.py
│   ├── apps.py           # App configuration
│   ├── admin.py          # Django admin configuration
│   ├── models.py         # Database models (Django convention)
│   ├── views.py          # View functions (Django convention - handles HTTP requests)
│   ├── urls.py           # URL patterns (Django convention - maps URLs to views)
│   ├── services/         # Business logic layer (optional but recommended)
│   │   ├── __init__.py
│   │   └── example_service.py
│   └── utils/            # Utility functions
│       ├── __init__.py
│       ├── response.py   # Standardized API responses
│       └── logger.py     # Logging utilities
├── templates/            # HTML templates (if needed)
├── static/               # Static files (CSS, JS, images)
└── media/                # User uploaded files
```

## Django Architecture Overview

### Models (`apps/models.py`)
- **Django Convention**: All models in a single `models.py` file
- Database models using Django ORM
- Contains model classes and helper functions for database operations

### Views (`apps/views.py`)
- **Django Convention**: View functions in `views.py` (not controllers)
- Handle HTTP requests and responses
- Process request data and return responses
- Similar to controllers in other frameworks

### URLs (`apps/urls.py`)
- **Django Convention**: URL patterns in `urls.py` (not routes.py)
- Maps URLs to view functions
- Each Django app typically has its own `urls.py`

### Services (`apps/services/`)
- **Optional but Recommended**: Business logic layer
- Separates business rules from views and models
- Can be reused across different views
- Makes code more testable and maintainable

### Utils (`apps/utils/`)
- Utility functions
- Response formatters
- Logging utilities

## Django vs Other Frameworks

| Concept | Django | Flask/Express |
|---------|--------|---------------|
| Request Handler | **Views** (`views.py`) | Controllers |
| URL Mapping | **URLs** (`urls.py`) | Routes |
| Database Models | **Models** (`models.py`) | Models |
| Business Logic | Services (optional) | Services |

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

## Running the Application

### Method 1: Using app.py (Optional Flask-like interface)
```bash
python app.py
```

With options:
```bash
python app.py --host 0.0.0.0 --port 8000 --debug
python app.py --migrate  # Run migrations before starting
```

### Method 2: Using manage.py (Traditional Django - Recommended)
```bash
python manage.py runserver
```

## Usage Example

### Creating a New Feature in Django

1. **Add a Model** (`apps/models.py`):
```python
from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

2. **Add Model Operations** (in `apps/models.py`):
```python
def get_all_items():
    return YourModel.objects.all()

def create_item(data):
    return YourModel.objects.create(**data)
```

3. **Add a Service** (`apps/services/your_service.py`):
```python
from apps.models import get_all_items, create_item

def get_all_items_service():
    # Business logic here
    return get_all_items()

def create_item_service(data):
    # Validation and business logic
    if not data.get('name'):
        raise ValueError("Name is required")
    return create_item(data)
```

4. **Add a View** (`apps/views.py`):
```python
from django.http import JsonResponse
from apps.services.your_service import get_all_items_service
from apps.utils.response import success_response

def get_items(request):
    items = get_all_items_service()
    return JsonResponse(success_response(data=items))
```

5. **Add URL Pattern** (`apps/urls.py`):
```python
from django.urls import path
from apps import views

urlpatterns = [
    path('items/', views.get_items, name='get_items'),
]
```

## Django Best Practices

1. **Models**: Keep all models in `models.py` (Django convention)
2. **Views**: Use function-based views or class-based views in `views.py`
3. **URLs**: Each app has its own `urls.py` that gets included in the main `config/urls.py`
4. **Services**: Use services for complex business logic (optional but recommended)
5. **Admin**: Register models in `admin.py` for Django admin interface

## API Response Format

All API responses follow a standardized format:

**Success Response:**
```json
{
    "success": true,
    "message": "Success",
    "status_code": 200,
    "data": { ... }
}
```

**Error Response:**
```json
{
    "success": false,
    "message": "Error message",
    "status_code": 400,
    "errors": [ ... ]
}
```

## Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## Development

- Run migrations: `python manage.py makemigrations && python manage.py migrate`
- Run tests: `python manage.py test`
- Access admin panel: `http://localhost:8000/admin/`
- API endpoints: `http://localhost:8000/api/`

## Key Django Concepts

- **Apps**: Self-contained modules (like `apps/` in this project)
- **Views**: Functions/classes that handle HTTP requests
- **URLs**: URL patterns that route requests to views
- **Models**: Database models using Django ORM
- **Admin**: Built-in admin interface for managing data
- **Migrations**: Database schema version control

## License

This is a template project. Feel free to use and modify as needed.
