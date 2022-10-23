rooms = int(input())
left_chairs = 0
enough_chairs_in_room = True

for room in range(1, rooms + 1):
    command = input().split()
    chairs, visitors = list(command[0]), int(command[1])
    if len(chairs) >= visitors:
        left_chairs += len(chairs) - visitors
        enough_chairs_in_room = True
    else:
        enough_chairs_in_room = False
        diff = abs(len(chairs) - visitors)
        print(f'{diff} more chairs needed in room {room}')
    rooms -= 1

if enough_chairs_in_room:
   print(f'Game On, {left_chairs} free chairs left')


