import requests
import os
import json


# Open a connection to login endpoint
class Transaction(object):
    def __init__(self):
        self.host = os.environ.get('AIM_API_HOST', 'https://aim-pro-dev.host.com/')
        self.url_login = os.environ.get(self.host, '/api/aim/login')
        self.username = os.environ.get('AIM_USER')
        self.password = os.environ.get('AIM_PASSWORD')
        self.headers = {'Content-type': 'application/json'}
        if self.username and self.password:
            self.login_data = dict(password=self.password)

    def run(self):
        url = self.host + self.url_login
        r = requests.post(url + '/' + self.username,
                          headers={'Content-Type': 'application/json'}, data=json.dumps(self.login_data)).text
        # for debug only
        print(r)



if __name__ == '__main__':
    trans = Transaction()
    trans.run()
