import requests
from time import time
from src.base_requests_class import BaseRequestsClass


class UserHandler(BaseRequestsClass):

    last_created_user_id = None
    create_user_dict = {"method": "POST", "endpoint": "/users"}
    get_user_dict = {"method": "GET", "endpoint": "/users/{user_id}"}
    update_user_dict = {"method": "PUT", "endpoint": "/users/{user_id}"}
    delete_user_dict = {"method": "DELETE", "endpoint": "/users/{user_id}"}


    def create_user(self, email, name="tester testowy", gender="male", status="active"):
        body = {"name": name, "gender": gender, "email": email, "status": status}
        res = self.send_request(self.create_user_dict["method"], self.create_user_dict["endpoint"], body)
        self.last_created_user_id = res.json()["data"]["id"]
        return res.json(), res.status_code, self.last_created_user_id

    def create_unique_user(self):
        unique_email = f"tester.testowy+{int(time())}@gmail.com"
        return self.create_user(unique_email)

    def get_user_by_id(self, id=None):
        if not id:
            id = self.last_created_user_id
        self.get_user_dict["endpoint"] = self.get_user_dict["endpoint"].format(user_id=id)
        print(self.get_user_dict, "           ", id)
        res = self.send_request(self.get_user_dict["method"], self.get_user_dict["endpoint"].format(user_id=id))
        return res.json(), res.status_code

    def update_user(self, user_id, name=None, email=None, status=None):
        body = {}
        if name:
            body["name"] = name
        if email:
            body["email"] = email
        if status:
            body["status"] = status
        res = self.send_request(self.get_user_dict["method"], self.get_user_dict["endpoint"].format(user_id=id), body)

        return res.json(), res.status_code

    def delete_user(self, user_id):
        res = self.send_request(self.get_user_dict["method"], self.get_user_dict["endpoint"].format(user_id=id))
        return res.status_code
