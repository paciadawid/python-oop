import pytest

from src.user_handler import UserHandler


@pytest.fixture
def create_user_and_return_id():
    user_handler = UserHandler()
    _, _, user_id = user_handler.create_unique_user()
    return user_id
