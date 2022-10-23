command = input()
command_list = []
dict_resources = {}

while command != 'stop':
    command_list.append(command)
    command = input()

for index in range(0, len(command_list), 2):
    resource = command_list[index]
    qty = int(command_list[index + 1])
    if resource not in dict_resources:
        dict_resources[resource] = qty
    else:
        dict_resources[resource] += qty

for resources, qty in dict_resources.items():
    print(f'{resources} -> {qty}')
