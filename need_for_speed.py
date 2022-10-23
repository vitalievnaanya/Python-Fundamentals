number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    if car not in cars:
        cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()

while command != 'Stop':
    data = command.split(' : ')

    if data[0] == 'Drive':
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])

        if cars[car]['fuel'] < fuel:
            print(f'Not enough fuel to make that ride')

        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]['mileage'] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")

    elif data[0] == 'Refuel':
        car = data[1]
        fuel = int(data[2])
        if cars[car]['fuel'] + fuel > 75:
            needed_fuel = 75 - cars[car]['fuel']
            cars[car]['fuel'] += needed_fuel
            print(f"{car} refueled with {needed_fuel} liters")
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif data[0] == 'Revert':
        car = data[1]
        kilometers = int(data[2])

        cars[car]['mileage'] -= kilometers

        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for key, data in cars.items():
    print(f"{key} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")