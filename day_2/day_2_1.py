with open('input_day2.txt', 'r') as file:
    input = [line.strip() for line in file]

red_max = 12  
green_max = 13 
blue_max = 14
games = list(range(1, 101))
counter = 0

for line in input:
    counter += 1
    line = line.replace("; ", ", ")
    line = line.replace(": ", ", ")
    line = line.split(", ")

    red = [int(r.replace(" red", "")) for r in line if "red" in r]
    green = [int(g.replace(" green", "")) for g in line if "green" in g]
    blue = [int(b.replace(" blue", "")) for b in line if "blue" in b]

    if max(red) > red_max or max(green) > green_max or max(blue) > blue_max:
        games.remove(counter)

print(sum(games))