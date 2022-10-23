usernames = input().split(', ')
validated = []

for username in usernames:
    if 3 <= len(username) <= 16:
        valid_username_check = True
        valid_username = ''
        for el in username:
            if el.isnumeric() or el.isalpha() or el == '-' or el == '_':
                valid_username += el
            else:
                valid_username_check = False
        if valid_username_check:
            validated.append(username)
for el in validated:
    print(el)
