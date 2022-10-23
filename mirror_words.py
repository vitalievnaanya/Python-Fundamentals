import re

text = input()
valid_matches = {}
pairs_count = 0
end_list = []

pattern = r'(?P<sur>#|@)(?P<word>[]A-Za-z]{3,})(?P=sur){2}(?P<word_two>[A-Za-z]{3,})(?P=sur)'

matches = re.finditer(pattern, text)

if matches is not None:
    for match in matches:
        pairs_count += 1
        matched_one = match.group('word')
        matched_two = match.group('word_two')
        reversed_word = matched_one[::-1]
        if reversed_word == matched_two:
            valid_matches[matched_one] = matched_two

if pairs_count == 0:
    print(f'No word pairs found!')
else:
    print(f"{pairs_count} word pairs found!")
if not valid_matches:
    print(f'No mirror words!')

else:
    print(f'The mirror words are:')
    for key, value in valid_matches.items():
        end_list += [f'{key} <=> {value}']
print(", ".join(end_list))
