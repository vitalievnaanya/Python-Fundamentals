right_str, left_str = input().split()

total_sum = 0

min_str = min(len(right_str), len(left_str))
max_str = max(len(right_str), len(left_str))

for i in range(min_str):
    left_num = ord(left_str[i])
    right_num = ord(right_str[i])
    total_sum += left_num * right_num


for i in range(min_str, max_str):
    if len(left_str) > len(right_str):
        left_num = ord(left_str[i])
        total_sum += left_num
    else:
        left_num = ord(right_str[i])
        total_sum += left_num


print(total_sum)
