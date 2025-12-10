"""
Main Application Entry Point
Similar to Flask's app.py, this is the main entry point for the Django application.
"""
import os
import sys
import django
from pathlib import Path

# Add the project root to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
from django.conf import settings


class DjangoApp:
    """
    Main Django Application Class
    Similar to Flask's app object, this class provides a centralized way
    to manage and configure the Django application.
    """
    
    def __init__(self):
        """Initialize the Django application."""
        self.settings_module = 'config.settings'
        self.wsgi_application = None
        self._setup()
    
    def _setup(self):
        """Setup Django environment."""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', self.settings_module)
        django.setup()
        self.wsgi_application = get_wsgi_application()
    
    def run(self, host='127.0.0.1', port=8000, debug=None):
        """
        Run the Django development server.
        
        Args:
            host: Host to bind to
            port: Port to bind to
            debug: Enable debug mode (uses settings.DEBUG if None)
        """
        if debug is not None:
            settings.DEBUG = debug
        
        from django.core.management.commands.runserver import Command as RunserverCommand
        runserver = RunserverCommand()
        runserver.handle(addrport=f'{host}:{port}', use_reloader=settings.DEBUG)
    
    def get_wsgi_app(self):
        """
        Get WSGI application for deployment.
        
        Returns:
            WSGI application
        """
        return self.wsgi_application
    
    def migrate(self):
        """Run database migrations."""
        execute_from_command_line(['manage.py', 'migrate'])
    
    def makemigrations(self):
        """Create database migrations."""
        execute_from_command_line(['manage.py', 'makemigrations'])
    
    def createsuperuser(self):
        """Create a superuser."""
        execute_from_command_line(['manage.py', 'createsuperuser'])


# Create app instance
app = DjangoApp()


if __name__ == '__main__':
    """
    Run the application directly.
    Usage: python app.py
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Django Application')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind to')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--migrate', action='store_true', help='Run migrations before starting')
    
    args = parser.parse_args()
    
    if args.migrate:
        print("Running migrations...")
        app.migrate()
    
    print(f"Starting Django development server on {args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=args.debug)

