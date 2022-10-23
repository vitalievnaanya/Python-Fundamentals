def calculate(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 // num2
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2

given_operator = input()
number_1 = int(input())
number_2 = int(input())

print(calculate(given_operator, number_1,number_2))