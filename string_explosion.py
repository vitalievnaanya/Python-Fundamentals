string = input()
strength = 0
i = 0

while i < len(string):
    if string[i] == ">":
        strength += int(string[i + 1])
    else:
        if strength > 0:
            string = string[:i] + string[i + 1:]
            i -= 1
            strength -= 1
    i += 1
print(string)


