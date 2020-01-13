class CustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print('Process Request', request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Process View', view_func, view_args, view_kwargs)

    def process_exception(self, request, exception):
        print('Process Expection')
        return None

    # def process_respones(self, response):
    #     print('Process Response', response)

    def process_template_response(self, request, response):
        print('Process Template response', request, response)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
