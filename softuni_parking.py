num_of_users = int(input())
users_dict = {}

while num_of_users > 0:
    command = input().split()
    num_of_users -= 1
    if 'register' in command:
        user_name, licence_num = command[1], command[2]
        if user_name not in users_dict:
            users_dict[user_name] = licence_num
            print(f'{user_name} registered {licence_num} successfully')
        else:
            for value in users_dict.values():
                print(f'ERROR: already registered with plate number {value}')
    elif 'unregister' in command:
        user_name = command[1]
        if user_name not in users_dict:
            print(f'ERROR: user {user_name} not found')
        else:
            users_dict.pop(user_name)
            print(f'{user_name} unregistered successfully')

for key, value in users_dict.items():
    print(f'{key} => {value}')