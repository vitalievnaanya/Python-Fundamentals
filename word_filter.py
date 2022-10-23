words = input().split()
characters = 0
even_words_characters = []

for word in words:
    for el in word:
        characters += 1
    if characters % 2 == 0:
        even_words_characters.append(word)
    else:
        characters = 0

for el in even_words_characters:
    print(el)

