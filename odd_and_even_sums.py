number = int(input())
num_string = str(number)
odd_nums = 0
even_nums = 0
for num in num_string:
    num = int(num)
    if num % 2 != 0:
        odd_nums += num
    elif num % 2 == 0:
        even_nums += num

print(f'Odd sum = {odd_nums}, Even sum = {even_nums}')

