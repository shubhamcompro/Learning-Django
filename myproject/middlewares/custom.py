class Custom(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(view_func, view_args, view_kwargs)

    def process_exception(self, request, exception):
        return None
