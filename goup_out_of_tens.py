def max_number(nums):
    max_num = max(nums)
    return max_num


def groups_of_ten(nums):
    groups = (max_number(nums) // 10)
    if max_number(nums) > groups * 10:
        groups = (groups + 1) * 10
    else:
        groups = groups * 10
    return groups


numbers = list(map(int, input().split(', ')))
numbers_as_string = list(map( str, numbers))
threshold = 10
while threshold <= groups_of_ten(numbers):
    new_list = []
    for el in numbers_as_string:
        number = int(el)
        if number <= threshold:
            new_list.append(el)

    print(f"Group of {threshold}'s: {list(map( int, new_list))}")

    for el in new_list:
        if el in numbers_as_string:
            numbers_as_string.remove(el)
    del new_list[:]

    threshold += 10

max_number(numbers)
groups_of_ten(numbers)

