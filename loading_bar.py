list_of_percent = []
list_of_points = []
def multiplator(num):
    num_as_string = str(num)
    for i in num_as_string:
        if int(num_as_string[0]) != 0:
            multi = int(num_as_string[0])
            return multi

def difference(num):
    if multiplator(num) != 0:
        diff = 10 - multiplator(num)
        return diff


def loading_bar(num):
    if num == 0:
        list_of_points = ['.'] * 10
        print(f'{num}% [{"".join(list_of_points)}]')
        print(f'Still loading...')

    elif 0 < num <= 90:
        list_of_percent = ['%'] * multiplator(num)
        list_of_points = ['.'] * difference(num)
        full_list = list_of_percent + list_of_points
        print(f'{num}% [{"".join(full_list)}]')
        print(f'Still loading...')

    elif num == 100:
        list_of_percent = ['%'] * 10
        print(f'{num}% Complete!')
        print(f'[{"".join(list_of_percent)}]')


number = int(input())
multiplator(number)
loading_bar(number)