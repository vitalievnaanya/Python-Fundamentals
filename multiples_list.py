first_num = int(input())
second_num = int(input())
according_list = []

for num in range(1, second_num * first_num + 1):
    if num % first_num == 0:
        according_list.append(num)
print(according_list)
