wagons = int(input())
train_list = [0] * wagons
command = input()

while command != 'End':
    data = command.split()
    if data[0] == 'add':
        train_list[-1] += int(data[1])

    elif data[0] == 'insert':
        index = int(data[1])
        joined_people = int(data[2])
        train_list[index] += joined_people

    elif data[0] == 'leave':
        left_wagon = int(data[1])
        left_people = int(data[2])
        train_list[left_wagon] -= left_people

    command = input()

print(train_list)