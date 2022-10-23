import re

text = input()
pattern = r'(?P<numbers>[\d]+)'
numbers = []

while text:
    match = re.findall(pattern, text)
    if match is not None:
        numbers += match
        text = input()

print(" ".join(numbers))