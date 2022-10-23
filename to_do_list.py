notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break
    data = command.split("-")
    importance, text = int(data[0]), data[1]
    notes.pop(importance)
    notes.insert(importance, text)

result = [el for el in notes if el != 0]
print(result)