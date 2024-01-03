with open('input_day10.txt', 'r') as file:
    input = [line.strip() for line in file]

start = []
for row, line in enumerate(input):
    for col, l in enumerate(line):
        if l == 'S':
            start = [row, col]

s_row = start[0]
s_col = start[1]

above = input[s_row-1][s_col] in ['|', '7', 'F']
below = input[s_row+1][s_col] in ['|', 'L', 'J']
left = input[s_row][s_col-1] in ['-', 'L', 'F'] 
right = input[s_row][s_col+1] in ['-', 'J', '7']
s = ''
if above and below:
    s = '|'
elif left and right:
    s = '-'
elif left and above:
    s = 'J'
elif right and above:
    s = 'L'
elif left and below:
    s = '7'
elif right and below:
    s = 'F'

dirs = {
    '|': [(-1,  0), (+1,  0)],
    'F': [(+1,  0), ( 0, +1)],
    'L': [(-1,  0), ( 0, +1)],
    '-': [( 0, +1), ( 0, -1)],
    '7': [(+1,  0), ( 0, -1)],
    'J': [(-1,  0), ( 0, -1)],
}

cur = [s_row, s_col]
prev = [-1, -1]
steps = 0

while True:
    c = input[cur[0]][cur[1]] if steps > 0 else s
    tmp = cur
    for dir in dirs[c]:
        new = [cur[0]+dir[0], cur[1]+dir[1]]
        if new != prev:
            cur = new
            break
    prev = tmp
    steps += 1
    if cur == start:
        break

print(steps/2)   
