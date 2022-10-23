def char_set (char_1, char_2):

    for char in range (ord(char_1) +1, ord(char_2)):

        print(chr(char), end=' ')


first_character = input()
second_character = input()

char_set(first_character, second_character)