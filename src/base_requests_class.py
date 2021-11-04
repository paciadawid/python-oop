from os import environ
import requests
import json

class BaseRequestsClass:

    base_url = "https://gorest.co.in/public/v1"

    def __init__(self, auth_token=None):
        token = environ.get("AUTH_TOKEN") if environ.get("AUTH_TOKEN") else auth_token
        self.auth_headers = {"Authorization": f"Bearer {token}"}

    def send_request(self, method, endpoint, body=None):
        print(endpoint)
        return requests.request(method.upper(), self.base_url + endpoint, headers=self.auth_headers, json=body)



    def __read_endpoint_map(self):
        with open("../endpoints_map.json") as file:
            endpoint_map = json.load(file)
        return endpoint_map