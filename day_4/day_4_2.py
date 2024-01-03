with open('input_day4.txt', 'r') as file:
    input = [line.strip() for line in file]

won_cards = {key: 1 for key in range(1, 213)}
card = 0
for line in input:
    card += 1
    line = line.replace(": ", " | ")
    line = line.split(" | ")
    
    winning = line[1].replace("  ", " ").strip().split(" ")
    elf = line[2].replace("  ", " ").strip().split(" ")

    card_below_counter = 0
    card_copy = card
    
    for e in elf:
        if e in winning:
            card_below_counter += 1
            
    for b in range(1, card_below_counter+1):
        card_copy += 1
        won_cards[card_copy] += 1 * won_cards[card]

print(sum(won_cards.values()))