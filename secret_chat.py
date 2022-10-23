concealed_message = input()
command = input()

while command != 'Reveal':
    data = command.split(':|:')
    if data[0] == 'InsertSpace':
        index = int(data[1])
        concealed_message = list(concealed_message)
        concealed_message.insert(index, ' ')
        print(''.join(concealed_message))

    elif data[0] == 'Reverse':
        substring = data[1]
        if substring not in concealed_message:
            print(f'error')
        else:
            concealed_message = concealed_message.replace(substring, '')
            reversed_substring = substring[::-1]
            concealed_message += reversed_substring
            print(concealed_message)

    elif data[0] == 'ChangeAll':
        concealed_message = concealed_message.replace(data[1], data[2])
        print(concealed_message)

    command = input()

print(f'You have a new text message: {"".join(concealed_message)}')