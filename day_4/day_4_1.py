with open('input_day4.txt', 'r') as file:
    input = [line.strip() for line in file]

row = 0
sum_points = 0
for line in input:
    row += 1
    line = line.replace(": ", " | ")
    line = line.split(" | ")
    
    winning = line[1].replace("  ", " ").strip().split(" ")
    elf = line[2].replace("  ", " ").strip().split(" ")

    counter = 0
    for e in elf:
        if e in winning:
            counter += 1
    if counter >= 1:
        points = 2**(counter-1)
    else:
        points = 0
    sum_points += points

print(sum_points)