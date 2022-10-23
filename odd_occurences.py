words = input().split(' ')
my_dict = {}

for word in words:
    word = word.lower()
    if word not in my_dict:
        my_dict[word] = 0

    my_dict[word] += 1

for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=' ')