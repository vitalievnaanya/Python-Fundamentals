all_characters = input().split()
chr_dict = {}

for words in all_characters:
    for letter in words:
        if letter not in chr_dict:
            chr_dict[letter] = 1
        else:
            chr_dict[letter] += 1


for character, quantity in chr_dict.items():

    print(f'{character} -> {quantity}')