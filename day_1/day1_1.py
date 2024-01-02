with open('input_day1.txt', 'r') as file:
    input = [line.strip() for line in file]

summed_values = 0
for line in input:
    newline = ''
    for c in line:
        if c.isdigit():
            newline += c
    twodigit = newline[0] + newline[-1]
    summed_values += int(twodigit)

print(summed_values)