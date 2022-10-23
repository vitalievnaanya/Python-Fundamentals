countries = input().split(", ")
capitals = input().split(", ")

capitals_dict = dict(zip(countries, capitals))

for country, capital in capitals_dict.items():
    print(f'{country} -> {capital}')