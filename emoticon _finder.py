text = input()
emoticons_list = []

for i in range(len(text)):
    emoticons = ''
    if text[i] == ":":
        emoticons += text[i]
        emoticons += text[i + 1]
        emoticons_list.append(emoticons)

for emoticon in emoticons_list:
    print(emoticon)

