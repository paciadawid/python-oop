import random

list_numbers = [1, 2, 3]


list_incremented = [number + 1 for number in list_numbers if number != 2]

print(list_incremented)

square_list = [number ** 2 for number in range(1, 11)]
print(square_list)

two_digit_odd_list = [number for number in range(10, 100) if number % 2]
print(two_digit_odd_list)

my_string = "i like pancakes"
vowels_from_pancakes = [letter for letter in my_string if letter in "aeiouy"]
print(vowels_from_pancakes)

matrix_3x3 = [[random.randint(0, 9) for _ in range(3)] for _ in range(10)]
print(matrix_3x3)

for line in matrix_3x3:
    print(line)
print(matrix_3x3[1][2])
