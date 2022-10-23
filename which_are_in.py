first_list = input().split(", ")
second_string = input().split(", ")
new_list = []

for word in first_list:
    for second_word in second_string:
        if word in second_word:
            new_list.append(word)

unique_list = []
for word in new_list:
    if word not in unique_list:
        unique_list.append(word)

print(unique_list)


