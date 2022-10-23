str_to_be_removed = input()
word = input()

while str_to_be_removed in word:
    word = word.replace(str_to_be_removed, '')
print(word)
