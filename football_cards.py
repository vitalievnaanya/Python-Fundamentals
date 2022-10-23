card = input()
card_as_a_list = card.split(" ")
team_a = 11
team_b = 11
previous_card_list = []

for i in range(len(card_as_a_list)):
    current_card = card_as_a_list[i]
    if current_card in previous_card_list:
        if 'A' in current_card:
            team_a += 1
        elif 'B' in current_card:
            team_b += 1
    previous_card_list.append(current_card)

    if 'A' in current_card:
        team_a -= 1
    elif 'B' in current_card:
        team_b -= 1
    if team_a < 7:
        break
    if team_b < 7:
        break
print(f'Team A - {team_a}; Team B - {team_b}')
if team_a < 7:
    print(f'Game was terminated')
if team_b < 7:
    print(f'Game was terminated')