from base_client import BaseClient
import requests
import json

class GetIDFromUsername(BaseClient):
    # URL vk api
    BASE_URL = 'https://api.vk.com/method/'
    # GET
    http_method = 'users.get'

    # Method, which is called when the exemplar is creating
    def __init__(self, uname):
        self.name = uname

    # Taking of GET-parameters of the request
    def get_params(self):
        return 'user_ids=' + self.name

    # Sending of the request to VK API
    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(self.http_method) + '?' + self.get_params())
        return self.response_handler(response)

    # Handling of the response from VK API
    def response_handler(self, response):
        try:
            str = json.loads(response.text)
            return str['response'][0]['uid']
        except:
            raise Exception("The response from VK API couldn't been handled.")