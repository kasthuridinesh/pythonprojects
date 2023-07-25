import requests


class HTTPHandler:
    def make_get_api_call(self, url):
        response = requests.get(url)
        return response

    def make_post_api_call(self, url, request_payload):
        pass

    def make_delete_api_call(self):
        pass





