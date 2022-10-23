food_in_gr = float(input()) * 1000
hay_in_gr = float(input()) * 1000
cover_in_gr = float(input()) * 1000
guinea_weight_in_gr = float(input()) * 1000
days = 30

for day in range(1, days + 1):
    food_in_gr -= 300
    days -= 1
    if day % 2 == 0:
        given_hay = food_in_gr * 5 / 100
        hay_in_gr -= given_hay
    if day % 3 == 0:
        given_cover = guinea_weight_in_gr / 3
        cover_in_gr -= given_cover

if food_in_gr > 0 and hay_in_gr > 0 and cover_in_gr > 0:
    print(f'Everything is fine! Puppy is happy! Food: {(food_in_gr/1000):.2f}, '
          f'Hay: {(hay_in_gr/1000):.2f}, Cover: {(cover_in_gr/1000):.2f}.')
else:
    print(f'Merry must go to the pet store!')

