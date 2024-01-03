with open('input_day3.txt', 'r') as file:
    input = [line.strip() for line in file]

row = -1  
stars_dict = {}

for line in input:
    row += 1
    col = -1
    sten = []
    
    for c in line:
        col += 1
        if c.isdigit():
            if col == 0 or not input[row][col-1].isdigit():
                sten.append(col)

            if col == len(line)-1 or not input[row][col+1].isdigit():
                sten.append(col)
                start = sten[0]
                end = sten[1]

                for r in range(row-1, row+2):
                    if r < 0 or r > len(input)-1:
                        continue
                    for p in range(start-1, end+2):
                        if p < 0 or p > len(line)-1:
                            continue
                        if input[r][p] == "*":
                            star_key = str(r) + "," + str(p)
                            star_num = int(line[start:end+1])
                            if star_key in stars_dict:
                                stars_dict.setdefault(star_key, []).append(star_num)
                            else: 
                                stars_dict[star_key] = [star_num]
            
                sten = []
                
                
gear_sum = 0
for d in stars_dict.values():
    if len(d) == 2:
        gear_sum += d[0] * d[1]

print(gear_sum)