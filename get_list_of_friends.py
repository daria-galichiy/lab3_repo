from base_client import BaseClient
import requests
import json
from datetime import datetime

class GetFriends(BaseClient):
    # URL vk api
    BASE_URL = 'https://api.vk.com/method/'
    # GET
    http_method = 'friends.get'

    # Method, which is called when the exemplar is creating
    def __init__(self, uid):
        self.uid = uid

    # Taking of GET-parameters of the request
    def get_params(self):
        return 'user_id=' + str(self.uid) + '&fields=bdate'

    # Sending of the request to VK API
    def _get_data(self, method, http_method):
        response = requests.get(self.generate_url(self.http_method) + '?' + self.get_params())
        return self.response_handler(response)

    # Handling of the response from VK API
    def response_handler(self, response):
        try:
            str = json.loads(response.text)
            friends = str.get('response')
            ages_amount = {}
            undef_age = []

            for friend in friends:
                try:
                    bdate = friend.get('bdate')
                    bdate = datetime.strptime(bdate, '%d.%m.%Y')
                except:
                    undef_age.append('#')
                    continue

                ndate = datetime.now()
                age = (int((ndate - bdate).days))//365

                if (age in ages_amount):
                    ages_amount[age] += '#'
                else:
                    ages_amount[age] = '#'

            return ages_amount, undef_age

        except:
            raise Exception("The response from VK API for friends couldn't been handled.")