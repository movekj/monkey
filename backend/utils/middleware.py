"""
    middleware
"""
from django.utils.deprecation import MiddlewareMixin
from .exception import *
from django.http import JsonResponse

class ExceptionHandleMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, ParamError):
            response = JsonResponse(
                status=400,
                data=dict(
                    status_code=400,
                    msg=exception.message,
                    errors=exception.error
                )
            )
            return response

        if isinstance(exception, PermError):
            response = JsonResponse(status=403, data=dict(status_code=401, msg=exception.message))
            return response

        if isinstance(exception, NotFoundError):
            response = JsonResponse(status=404, data=dict(status_code=404, msg=exception.message))
            return response
