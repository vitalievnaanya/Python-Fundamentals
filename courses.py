command = input()
course_dict = {}


while command != 'end':
    course, student = command.split(' : ')
    if course not in course_dict:
        course_dict[course] = [student]
    else:
        course_dict[course].append(student)

    command = input()
for key, value in course_dict.items():
    print(f'{key}: {len(value)}')
    for student in value:
        print(f'-- {student}')

