import re

pattern = r"\+359(?P<separator>[\s|-])2(?P=separator)\d{3}(?P=separator)\d{4}\b"
phones = input()

valid_phones = re.finditer(pattern, phones)
output = []
for phone in valid_phones:
    output.append(phone.group())

print(", ".join(output))


