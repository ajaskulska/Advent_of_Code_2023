with open('input_day6.txt', 'r') as file:
    input = [line.strip().split()[1:] for line in file]

race_time = int(''.join(input[0]))
race_record = int(''.join(input[1]))

win_possib = 0

for s in range(race_time + 1):
    dist_travel = (race_time - s) * s
    if dist_travel > race_record:
        win_possib += 1

print(win_possib)