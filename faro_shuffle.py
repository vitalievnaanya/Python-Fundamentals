cards = input().split( )
shuffle_times = int(input())
half_size = len(cards) // 2

for i in range(shuffle_times):
    left_side = cards[:half_size]
    right_side = cards[half_size:]

    faro_cards = []

    for j in range (len(right_side)):
        faro_cards.append(left_side[j])
        faro_cards.append(right_side[j])

    cards = faro_cards

print(cards)