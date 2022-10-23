import re

text = input()

pattern = r'(?P<url>www\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'

valid_websites = []

while text:
    matches = re.finditer(pattern, text)

    for match in matches:
        valid_websites.append(match.group('url'))

    text = input()

for url in valid_websites:
    print(url)
