students_data = input()
my_dict = {}

while ":" in students_data:
    student_name, student_id, course = students_data.split(':')
    if course not in my_dict:
        my_dict[course] = {}
    my_dict[course][student_id] = student_name
    students_data = input()

searched_course = students_data
searched_course = searched_course.split('_')
searched_course = " ".join(searched_course)
for course in my_dict:
    if course == searched_course:
        for student_id, student_name in my_dict[course].items():
            print(f'{student_name} - {student_id}')