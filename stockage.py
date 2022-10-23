command = input()
stock_dict = {}

while command != "statistics":
    product, quantity = command.split(": ")
    if product not in stock_dict:
        stock_dict[product] = int(quantity)
    else:
        stock_dict[product] += int(quantity)
    command = input()

print('Products in stock:')

for key, value in stock_dict.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(stock_dict)}')
print(f'Total Quantity: {sum(stock_dict.values())}')
