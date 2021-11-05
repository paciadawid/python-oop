import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def another_fruit():
    return Fruit("ornage")

@pytest.fixture
def fruit_basket(my_fruit, another_fruit):
    return [another_fruit, my_fruit]

# @pytest.fixture
# def fruit_super_basket(fruit_basket):
#     return [Fruit("banana"), my_fruit, fruit_basket]


def test_my_fruit_in_basket(fruit_basket):
    print(fruit_basket)