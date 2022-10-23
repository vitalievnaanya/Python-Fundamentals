characters = input().split(', ')
ascii_dict = {}

for ch in characters:
    ascii_dict[ch] = ord(ch)
print(ascii_dict)