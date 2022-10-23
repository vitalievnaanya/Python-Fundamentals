class Party:
    def __init__(self):
        self.people = []


party = Party()
people_at_the_party = input()


while people_at_the_party != 'End':
    party.people.append(people_at_the_party)

    people_at_the_party = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
