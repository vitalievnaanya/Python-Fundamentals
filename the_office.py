employees_grade = [int(el) for el in input().split()]
factor = int(input())

happiness = [el*factor for el in employees_grade]
average = sum(employees_grade) / len(employees_grade)

happy_employees = [el for el in employees_grade if el >= average]

if len(happy_employees) >= len(employees_grade)/2:
    print(f'Score: {len(happy_employees)}/{len(employees_grade)}.'
          f' Employees are happy!')

else:
    print(f'Score: {len(happy_employees)}/{len(employees_grade)}.'
          f' Employees are not happy!')