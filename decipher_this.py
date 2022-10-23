def secret_message(word: str):
    num_as_str = ''
    left_word = []

    for ch in word:
        if ch.isnumeric():
            num_as_str += ch
        else:
            left_word.append(ch)

    left_word.insert(0, chr(int(num_as_str)))
    return left_word

def decipher_word(word: str):
    new_word = secret_message(word)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    return ''.join(new_word)

deciphered_list = []
secret_words = input().split()
for word in secret_words:
    word = decipher_word(word)
    deciphered_list.append(word)
print(' '.join(deciphered_list))


