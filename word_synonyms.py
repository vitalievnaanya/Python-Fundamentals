n = int(input())
dict_synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in dict_synonyms:
        dict_synonyms[word] = []
    dict_synonyms[word].append(synonym)

for key, value in dict_synonyms.items():
    print(f'{key} - {", ".join(value)}')