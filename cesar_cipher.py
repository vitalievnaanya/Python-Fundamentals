message = input()
decipher_message = ''

for letter in message:
    current_letter = ord(letter) + 3
    decipher_message += chr(current_letter)

print(decipher_message)