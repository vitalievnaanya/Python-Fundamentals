products_data = input()
dict_products = {}


while products_data != 'buy':
    data_list = []
    product, price, qty = products_data.split()
    data_list.append(price)
    data_list.append(int(qty))
    if product not in dict_products:
        dict_products[product] = data_list
    else:
        single_dict = dict_products.get(product)
        single_dict[0] = float(price)
        single_dict[1] += int(qty)
        dict_products[product] = single_dict

    products_data = input()

for key, value in dict_products.items():
    last_value = float(value[0]) * float(value[1])
    print(f'{key} -> {float(last_value):.2f}')
