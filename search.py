n = int(input())
word = input()
list_of_sentences =[]
matching_word_list = []

for _ in range(n):
    sentence = input()
    list_of_sentences.append(sentence)
    if word in sentence:
        matching_word_list.append(sentence)

print(list_of_sentences)
print(matching_word_list)