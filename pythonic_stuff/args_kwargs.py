def add_values(*args):
    result = 0
    for number in args:
        result += number
    return result


result = add_values()


def create_dictionary(gender, **kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value
    return my_dict


my_dict = create_dictionary(gender="M", name="Test", age=21, city="Krakow")
print(my_dict)
