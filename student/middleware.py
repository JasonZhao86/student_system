from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
import time


class TimeStatisticsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse("index"):
            return None

        start = time.time()
        response = func(request)
        end = time.time()
        print("process view: {:.2f}s".format(end - start))
        return response

    def process_response(self, request, response):
        cost = time.time() - self.start
        print("request to response cost :{:.2f}".format(cost))
        return response

    def process_template_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        pass
