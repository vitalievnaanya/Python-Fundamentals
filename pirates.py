command = input()
cities = {}

while command != 'Sail':
    city, population, gold = command.split('||')
    command = input()
    if city not in cities:
        cities[city] = {'population': int(population), 'gold': int(gold)}
    else:
        cities[city]['population'] += int(population)
        cities[city]['gold'] += int(gold)

command = input()

while command != 'End':
    data = command.split('=>')
    if data[0] == 'Plunder':
        town = data[1]
        people = int(data[2])
        gold = int(data[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold

        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            del cities[town]
            print(f'{town} has been wiped off the map!')

    elif data[0] == 'Prosper':
        town = data[1]
        gold = int(data[2])

        if gold < 0:
            print(f'Gold added cannot be a negative number!')
            command = input()
            continue

        cities[town]['gold'] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')

    command = input()

if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for key, data in cities.items():
        print(f'{key} -> Population: {data["population"]} citizens, Gold: {data["gold"]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
