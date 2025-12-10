"""
Django Views
Handle HTTP requests and responses.
In Django, views are equivalent to controllers in other frameworks.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from apps.services import example_service
from apps.utils.response import success_response, error_response


@require_http_methods(["GET"])
def get_example(request):
    """
    Get all examples.
    """
    try:
        examples = example_service.get_all_examples()
        return JsonResponse(success_response(data=examples), status=200)
    except Exception as e:
        return JsonResponse(error_response(str(e)), status=500)


@require_http_methods(["GET"])
def get_example_by_id(request, id):
    """
    Get example by ID.
    """
    try:
        example = example_service.get_example_by_id(id)
        if example:
            return JsonResponse(success_response(data=example), status=200)
        return JsonResponse(error_response("Example not found"), status=404)
    except Exception as e:
        return JsonResponse(error_response(str(e)), status=500)


@csrf_exempt
@require_http_methods(["POST"])
def create_example(request):
    """
    Create a new example.
    """
    try:
        data = json.loads(request.body)
        example = example_service.create_example(data)
        return JsonResponse(success_response(data=example, message="Example created successfully"), status=201)
    except json.JSONDecodeError:
        return JsonResponse(error_response("Invalid JSON"), status=400)
    except Exception as e:
        return JsonResponse(error_response(str(e)), status=500)


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def update_example(request, id):
    """
    Update an example.
    """
    try:
        data = json.loads(request.body)
        example = example_service.update_example(id, data)
        if example:
            return JsonResponse(success_response(data=example, message="Example updated successfully"), status=200)
        return JsonResponse(error_response("Example not found"), status=404)
    except json.JSONDecodeError:
        return JsonResponse(error_response("Invalid JSON"), status=400)
    except Exception as e:
        return JsonResponse(error_response(str(e)), status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_example(request, id):
    """
    Delete an example.
    """
    try:
        deleted = example_service.delete_example(id)
        if deleted:
            return JsonResponse(success_response(message="Example deleted successfully"), status=200)
        return JsonResponse(error_response("Example not found"), status=404)
    except Exception as e:
        return JsonResponse(error_response(str(e)), status=500)

