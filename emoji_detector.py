import re

num_pattern = r'\d'

pattern = r'(?P<sur>:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=sur)'

text = input()

cool_threshold = 1
emojis_count = 0
valid_emojis = []

for num in re.findall(num_pattern, text):
    cool_threshold *= int(num)

print(f'Cool threshold: {cool_threshold}')

emojis = re.finditer(pattern, text)

for emoji in emojis:
    emojis_count += 1
    emoji_coolness = sum([ord(letter) for letter in emoji.group('emoji')])
    if emoji_coolness >= cool_threshold:
        valid_emojis.append(emoji.group())

print(f'{emojis_count} emojis found in the text. The cool ones are:')

for emoji in valid_emojis:
    print(emoji)
