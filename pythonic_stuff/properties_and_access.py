class TestClass:
    __selector = "test"
    _selector = "test"

    @property
    def selector(self):
        return self.__selector

    @selector.setter
    def selector(self, value):
        self.__selector = value


test_class = TestClass()
test_class.selector = 1


class TestClass2:
    __selector = "test"
    _selector_protected = "test"

    def get_selector(self):
        return self.__selector

    def set_selector(self, value):
        self.__selector = value


test_class2 = TestClass2()
test_class2.set_selector(1)
