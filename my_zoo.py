class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, specie, names):
        if specie == 'mammal':
            self.mammals.append(names)
        elif specie == 'fish':
            self.fishes.append(names)
        elif specie == 'bird':
            self.birds.append(names)

        Zoo.__animals += 1

    def get_info(self, specie):
        result = ''
        if specie == 'mammal':
            result += f' Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif specie == 'fish':
            result += f' Fishes in {self.name}: {", ".join(self.fishes)}\n'
        elif specie == 'bird':
            result += f' Birds in {self.name}: {", ".join(self.birds)}\n'

        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for x in range(count):
    species, names = input().split()
    zoo.add_animals(species, names)

info = input()
print(zoo.get_info(info))
