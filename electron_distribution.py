electrons = int(input())

config_electrons = []
current_layer = 1

while electrons > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)

    if electrons >= current_layer_electrons:
        config_electrons.append(current_layer_electrons)
    else:
        config_electrons.append(electrons)

    electrons -= current_layer_electrons
    current_layer += 1
print(config_electrons)
