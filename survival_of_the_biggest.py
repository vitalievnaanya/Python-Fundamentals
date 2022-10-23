numbers_list = input().split()
n = int(input())

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

for x in range(n):
    min_number = min(numbers_list)
    numbers_list.remove(min_number)

for j in range(len(numbers_list)):
    numbers_list[j] = str(numbers_list[j])

print(', '.join(numbers_list))
