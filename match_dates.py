import re

pattern = r"\b(?P<Day>\d{2})\b(?P<separator>[/.-])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"
dates = input()

valid_dates = re.finditer(pattern, dates)
for date in valid_dates:
    curr_date = date.groupdict()
    print(f"Day: {curr_date['Day']}, Month: {curr_date['Month']}, Year: {curr_date['Year']}")
