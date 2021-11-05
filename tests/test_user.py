from src.user_handler import UserHandler


class TestUser:
    user_handler = UserHandler()

    def test_create_user(self):
        body, status_code, user_id = self.user_handler.create_unique_user()
        assert status_code == 201, body
        body, status_code = self.user_handler.get_user_by_id(user_id)
        assert status_code == 200, body
        assert body["data"]["id"] == user_id, body

    def test_update_user(self):
        _, _, user_id = self.user_handler.create_unique_user()
        body, status_code = self.user_handler.update_user(user_id, name="Nietester Nietestowy")
        assert status_code == 200, body
        assert body["data"]["id"] == user_id, body
        assert body["data"]["name"] == "Nietester Nietestowy", body

    def test_delete_user(self):
        _, _, user_id = self.user_handler.create_unique_user()
        status_code = self.user_handler.delete_user(user_id)
        assert status_code == 204
        _, status_code = self.user_handler.get_user_by_id(user_id)
        assert status_code == 404
