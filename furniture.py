import re

pattern = r'^>>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$'

bought_furniture = []
total_sum = 0

text = input()
while text != 'Purchase':
    matches = re.match(pattern, text)

    if matches is not None:
        furniture = matches.group('furniture')
        price = float(matches.group('price'))
        qty = int(matches.group('quantity'))

        bought_furniture.append(furniture)
        total_sum += price * qty

    text = input()

print(f'Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_sum:.2f}')