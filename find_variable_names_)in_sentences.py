import re

text = input()

pattern = r'\b\_(?P<variable>[A-Za-z0=9]+)\b'
matches = re.finditer(pattern, text)
valid_username = []

for match in matches:
    valid_username.append(match.group('variable'))
print(",".join(valid_username))