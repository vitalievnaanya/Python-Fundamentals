import re

text = input()
valid_emails = []

pattern = r'\s(?P<email>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*)\@(?P<host>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z]+' \
          r'[A-Za-z]*)+))'

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group('email'))

