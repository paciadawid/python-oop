from time import time

from src.base_requests_class import BaseRequestsClass


class UserHandler(BaseRequestsClass):
    __last_created_user_id = None
    __create_user_dict = {"method": "POST", "endpoint": "/users"}
    __get_user_dict = {"method": "GET", "endpoint": "/users/{user_id}"}
    __update_user_dict = {"method": "PUT", "endpoint": "/users/{user_id}"}
    __delete_user_dict = {"method": "DELETE", "endpoint": "/users/{user_id}"}

    def create_user(self, email, name="tester testowy", gender="male", status="active"):
        body = {"name": name, "gender": gender, "email": email, "status": status}
        res = self.send_request(self.__create_user_dict["method"], self.__create_user_dict["endpoint"], body)
        self.__last_created_user_id = res.json()["data"]["id"]
        return res.json(), res.status_code, self.__last_created_user_id

    def create_unique_user(self):
        unique_email = f"tester.testowy+{int(time())}@gmail.com"
        return self.create_user(unique_email)

    def get_user_by_id(self, user_id=None):
        if not user_id:
            user_id = self.__last_created_user_id
        res = self.send_request(self.__get_user_dict["method"],
                                self.__get_user_dict["endpoint"].format(user_id=user_id))
        return res.json(), res.status_code

    def update_user(self, user_id, **kwargs):
        body = {}
        for key, value in kwargs.items():
            body[key] = value
        res = self.send_request(self.__update_user_dict["method"],
                                self.__update_user_dict["endpoint"].format(user_id=user_id), body)

        return res.json(), res.status_code

    def delete_user(self, user_id):
        res = self.send_request(self.__delete_user_dict["method"],
                                self.__delete_user_dict["endpoint"].format(user_id=user_id))
        return res.status_code

    @property
    def last_created_user_id(self):
        return self.__last_created_user_id

    @last_created_user_id.setter
    def last_created_user_id(self, value):
        self.__last_created_user_id = value
