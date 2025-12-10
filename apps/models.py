"""
Django Models
Database models and operations.
"""
from django.db import models
from apps.utils.logger import get_logger

logger = get_logger(__name__)


class Example(models.Model):
    """
    Example Django Model
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'examples'
        ordering = ['-created_at']
        verbose_name = 'Example'
        verbose_name_plural = 'Examples'

    def __str__(self):
        return self.name

    def to_dict(self):
        """
        Convert model instance to dictionary.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active,
        }


# Model Operations (Repository Pattern)
# These functions provide a service layer for model operations
def get_all_examples():
    """
    Get all active examples.
    """
    try:
        examples = Example.objects.filter(is_active=True)
        return [example.to_dict() for example in examples]
    except Exception as e:
        logger.error(f"Error in get_all_examples: {str(e)}")
        raise


def get_example_by_id(id):
    """
    Get example by ID.
    """
    try:
        example = Example.objects.get(id=id, is_active=True)
        return example.to_dict()
    except Example.DoesNotExist:
        return None
    except Exception as e:
        logger.error(f"Error in get_example_by_id: {str(e)}")
        raise


def create_example(data):
    """
    Create a new example.
    """
    try:
        example = Example.objects.create(
            name=data.get('name'),
            description=data.get('description', ''),
            is_active=data.get('is_active', True)
        )
        return example.to_dict()
    except Exception as e:
        logger.error(f"Error in create_example: {str(e)}")
        raise


def update_example(id, data):
    """
    Update an example.
    """
    try:
        example = Example.objects.get(id=id, is_active=True)
        
        if 'name' in data:
            example.name = data['name']
        if 'description' in data:
            example.description = data.get('description', '')
        if 'is_active' in data:
            example.is_active = data['is_active']
        
        example.save()
        return example.to_dict()
    except Example.DoesNotExist:
        return None
    except Exception as e:
        logger.error(f"Error in update_example: {str(e)}")
        raise


def delete_example(id):
    """
    Soft delete an example (set is_active=False).
    """
    try:
        example = Example.objects.get(id=id, is_active=True)
        example.is_active = False
        example.save()
        return True
    except Example.DoesNotExist:
        return False
    except Exception as e:
        logger.error(f"Error in delete_example: {str(e)}")
        raise

