words = input().split(" ")
searched_word = input()
palindrome = []

for el in words:
    if el == el[::-1]:
        palindrome.append(el)

print(palindrome)
print(f'Found palindrome {palindrome.count(searched_word)} times')
