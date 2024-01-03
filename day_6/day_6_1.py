with open('input_day6.txt', 'r') as file:
    input = [line.strip().split()[1:] for line in file]

time_dist = list(zip(input[0], input[1]))

result = 1
for td in time_dist:
    
    race_time = int(td[0])
    record = int(td[1])
    win_possib = 0

    for s in range(int(td[0])+1):
        dist_travel = (race_time - s) * s
        if dist_travel > record:
            win_possib += 1
    
    result = result * win_possib

print(result)