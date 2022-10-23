groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    data = command.split(" ")

    if data[0] == "Urgent":
        if not data[1] in groceries:
            groceries.insert(0, data[1])

    elif data[0] == "Unnecessary":
        if data[1] in groceries:
            groceries.remove(data[1])

    elif data[0] == "Correct":
        old_item = data[1]
        new_item = data[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item

    elif data[0] == "Rearrange":
        if data[1] in groceries:
            groceries.remove(data[1])
            groceries.append(data[1])

    command = input()

print(", ".join(groceries))