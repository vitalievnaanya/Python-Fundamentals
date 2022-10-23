letters = input()
new_str = f'{letters[0]}'

for i in range(1, len(letters)):

    if letters[i] != letters[i - 1]:
        new_str += letters[i]
print(new_str)