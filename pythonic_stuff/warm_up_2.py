def calculate_result(list_of_numbers):
    for i in list_of_numbers:
        for j in list_of_numbers:
            if i + j == 2020 and i != j:
                return i*j


with open("../input.txt") as file:
    list_of_numbers = [int(line) for line in file.readlines()]

    # list_of_numbers = []
    # for line in file.readlines():
    #     list_of_numbers.append(int(line))


result = calculate_result(list_of_numbers)
print(result)
