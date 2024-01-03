with open('input_day3.txt', 'r') as file:
    input = [line.strip() for line in file]

row = -1  
to_sum = []
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
                is_special = False
                
                
                for r in range(row-1, row+2):
                    if r < 0 or r > len(input)-1:
                        continue
                    for p in range(start-1, end+2):
                        if p < 0 or p > len(line)-1:
                            continue
                        if not input[r][p].isdigit() and input[r][p] != ".":
                            is_special = True
                            if is_special: 
                                to_sum.append(int(line[start:end+1]))
                            
                sten = []



print(sum(to_sum))