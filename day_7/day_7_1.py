with open('input_day7.txt', 'r') as file:
    input = [line.strip() for line in file]

def upper_hand(hand):
    card_counter = {}
    for char in hand:
        card_counter[char] = card_counter.get(char, 0) + 1

    if len(card_counter) == 5:
        # high card
        hand_type = 1
    elif len(card_counter) == 4:
        # one pair
        hand_type = 2
    elif len(card_counter) == 3:
        if (3 in card_counter.values()):
             # three of a kind
             hand_type = 4
        else:
            # two pair
            hand_type = 3
    elif len(card_counter) == 2:
        if (4 in card_counter.values()):
            # four of a kind
            hand_type = 6
        else:
            # full house
            hand_type = 5
    else:
        # five of a kind
        hand_type = 7

    return(hand_type)


card_strength = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

total = 0
for row, line in enumerate(input):
    line = line.split()
    hand = line[0]
    bid = int(line[1])

    no_of_wins = 1 # rank
    for new_row, new_line in enumerate(input):
        if new_row == row:
            continue
        new_line = new_line.split()
        hand_2 = new_line[0]

        hand_type = upper_hand(hand)
        hand_2_type = upper_hand(hand_2)
   
        if hand_type > hand_2_type:
            no_of_wins += 1
        elif hand_type < hand_2_type:
            continue
        elif hand_type == hand_2_type:
            hand_char = [c for c in hand]
            hand_2_char = [c for c in hand_2]
            for i in range(5):
                if card_strength[hand_char[i]] > card_strength[hand_2_char[i]]:
                    no_of_wins += 1
                    break
                elif card_strength[hand_char[i]] < card_strength[hand_2_char[i]]:
                    break

    total += bid * no_of_wins

print(total)

