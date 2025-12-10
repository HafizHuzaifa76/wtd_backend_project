"""
Response utilities for standardized API responses.
"""


def success_response(data=None, message="Success", status_code=200):
    """
    Create a standardized success response.
    
    Args:
        data: Response data
        message: Success message
        status_code: HTTP status code
    
    Returns:
        dict: Standardized response
    """
    response = {
        'success': True,
        'message': message,
        'status_code': status_code,
    }
    
    if data is not None:
        response['data'] = data
    
    return response


def error_response(message="An error occurred", status_code=400, errors=None):
    """
    Create a standardized error response.
    
    Args:
        message: Error message
        status_code: HTTP status code
        errors: List of error details
    
    Returns:
        dict: Standardized error response
    """
    response = {
        'success': False,
        'message': message,
        'status_code': status_code,
    }
    
    if errors:
        response['errors'] = errors
    
    return response

