data = input().split(" ")
my_dict = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = data[index +1]
    my_dict[key] = int(value)

print(my_dict)
