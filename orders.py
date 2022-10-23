def price(product, quantity):
    if product == 'water':
        return quantity
    elif product == 'coffee':
        return quantity * 1.50
    elif product == 'coke':
        return  quantity * 1.40
    elif product == 'snacks':
        return  quantity * 2

product_type = input()
amount = int(input())

total_price = price(product_type, amount)
print(f'{total_price:.2f}')