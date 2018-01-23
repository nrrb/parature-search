from django.contrib.auth import get_user
from .models import Record

class LogAllMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # We don't want to log admin site requests, as we'll look at these logs from the admin site
            response = self.get_response(request)
            return response

        meta = request.META

        newRecord = Record(
            path = request.path,
            user = get_user(request),
            query_string = meta['QUERY_STRING'],
            user_address = meta['HTTP_X_REAL_IP'],
            )
        newRecord.save()
        response = self.get_response(request)
        return response
