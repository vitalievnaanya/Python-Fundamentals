n_lines = int(input())
students_dict = {}
high_grade_students = {}

for n in range(n_lines):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

for key, value in students_dict.items():
    average_score = sum(value) / len(value)
    if average_score >= 4.5:
        high_grade_students[key] = average_score

for key, value in high_grade_students.items():
    print(f'{key} -> {value:.2f}')



