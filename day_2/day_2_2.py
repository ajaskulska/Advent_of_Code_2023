with open('input_day2.txt', 'r') as file:
    input = [line.strip() for line in file]

triplepower = []

for line in input:

    line = line.replace("; ", ", ")
    line = line.replace(": ", ", ")
    line = line.split(", ")

    red = max([int(r.replace(" red", "")) for r in line if "red" in r])
    green = max([int(g.replace(" green", "")) for g in line if "green" in g])
    blue = max([int(b.replace(" blue", "")) for b in line if "blue" in b])
    
    power = red * green * blue
    triplepower.append(power)
    
print(sum(triplepower))