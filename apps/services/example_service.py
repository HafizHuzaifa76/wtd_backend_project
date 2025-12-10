"""
Example Service
Contains business logic for example operations.
Services separate business logic from views and models.
"""
from apps.models import (
    get_all_examples as model_get_all,
    get_example_by_id as model_get_by_id,
    create_example as model_create,
    update_example as model_update,
    delete_example as model_delete
)
from apps.utils.logger import get_logger

logger = get_logger(__name__)


def get_all_examples():
    """
    Get all examples.
    Business logic layer - can add filtering, sorting, etc.
    """
    try:
        # Business logic here (e.g., add default sorting, filtering)
        examples = model_get_all()
        return examples
    except Exception as e:
        logger.error(f"Error getting all examples: {str(e)}")
        raise


def get_example_by_id(id):
    """
    Get example by ID.
    """
    try:
        example = model_get_by_id(id)
        return example
    except Exception as e:
        logger.error(f"Error getting example by id {id}: {str(e)}")
        raise


def create_example(data):
    """
    Create a new example.
    Business logic: validation, data transformation, etc.
    """
    try:
        # Validate data
        if not data.get('name'):
            raise ValueError("Name is required")
        
        # Business logic here (e.g., set defaults, transform data)
        example = model_create(data)
        return example
    except Exception as e:
        logger.error(f"Error creating example: {str(e)}")
        raise


def update_example(id, data):
    """
    Update an example.
    """
    try:
        # Business logic here (e.g., validate updates, audit logging)
        example = model_update(id, data)
        return example
    except Exception as e:
        logger.error(f"Error updating example {id}: {str(e)}")
        raise


def delete_example(id):
    """
    Delete an example.
    """
    try:
        # Business logic here (e.g., check dependencies, soft delete)
        deleted = model_delete(id)
        return deleted
    except Exception as e:
        logger.error(f"Error deleting example {id}: {str(e)}")
        raise

