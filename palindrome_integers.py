def if_is_palindrome(numbers):
    splited_list = numbers.split(", ")

    for el in splited_list:
        if (el == el[:: -1]):
            print(True)
        else:
            print(False)



integer_list = input()

if_is_palindrome(integer_list)
