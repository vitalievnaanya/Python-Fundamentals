raw_activation_key = input()

instruction = input()

while instruction != 'Generate':
    data = instruction.split('>>>')

    if data[0] == 'Contains':
        substring = data[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif data[0] == 'Flip':
        command = data[1]
        start_index = int(data[2])
        end_index = int(data[3])

        first_string_part = raw_activation_key[:start_index]
        part_to_change = raw_activation_key[start_index:end_index]
        last_part = raw_activation_key[end_index:]

        if command == 'Upper':
            part_to_change = part_to_change.upper()
            raw_activation_key = first_string_part + part_to_change + last_part
            print(raw_activation_key)
        elif command == 'Lower':
            part_to_change = part_to_change.lower()
            raw_activation_key = first_string_part + part_to_change + last_part
            print(raw_activation_key)

    elif data[0] == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])

        first_string_part = raw_activation_key[:start_index]
        part_to_change = raw_activation_key[start_index:end_index]
        last_part = raw_activation_key[end_index:]

        raw_activation_key = first_string_part + last_part
        print(raw_activation_key)

    instruction = input()

print(f'Your activation key is: {raw_activation_key}')