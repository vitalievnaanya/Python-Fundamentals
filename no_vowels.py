vowels = ['a', 'o', 'u', 'e', 'i']

given_string = input()
print("".join([el for el in given_string if el.lower() not in vowels]))