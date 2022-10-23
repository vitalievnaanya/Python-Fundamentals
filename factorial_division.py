def first_factorial(num_1):
    for n in range(1, num_1):
        num_1 *= n
    return num_1


def second_factorial(num_2):
    for n in range(1, num_2):
        num_2 *= n
    return num_2


def division(num_1, num_2):
    div = num_1 / num_2
    return div


number_1 = int(input())
number_2 = int(input())
first_factorial(number_1)
second_factorial(number_2)
print(f'{division(first_factorial(number_1), second_factorial(number_2)):.2f}')