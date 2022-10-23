n = int(input())
positive_list = []
negative_list = []
positive_num_counter = 0

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_num_counter += 1
        positive_list.append(number)
    else:
        negative_list.append(number)
print(positive_list)
print(negative_list)
print(f'Count of positives: {positive_num_counter}')
print(f'Sum of negatives: {sum(negative_list)}')