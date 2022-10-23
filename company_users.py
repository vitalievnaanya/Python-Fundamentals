command = input()
company_dict = {}

while command != 'End':
    company_name, employee_id = command.split(' -> ')
    if company_name not in company_dict:
        company_dict[company_name] = [employee_id]
    elif company_name in company_dict:
        value = company_dict.get(company_name)
        if employee_id not in value:
            company_dict[company_name].append(employee_id)

    command = input()

for company_name, employee_id in company_dict.items():
    print(f'{company_name}')
    for value in employee_id:
        print(f'-- {value}')