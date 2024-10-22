from django.utils.deprecation import MiddlewareMixin
import logging

class DisableCSRFCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Disable CSRF check for requests starting with /api/
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
            
class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logging.info(f"Request method: {request.method}")
        logging.info(f"Request path: {request.path}")
        logging.info(f"Request headers: {request.headers}")
        # Log request body if needed
        if request.method in ['POST', 'PUT', 'PATCH']:
            logging.info(f"Request body: {request.body.decode('utf-8')}")            