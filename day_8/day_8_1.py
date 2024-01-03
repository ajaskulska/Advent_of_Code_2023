with open('input_day8.txt', 'r') as file:
    input = [line.strip() for line in file]

instructions = [i for i in input[0]]
nodes = input[2:]
nodes_dict = {}
for n in nodes:
    curr = n.replace("= (", " ").replace(", ", " ").replace(")", " ").split()
    nodes_dict[curr[0]] = [curr[1], curr[2]]

steps = 0
state = 'AAA'
while state != 'ZZZ':
    dir = instructions[steps % len(instructions)]
    steps += 1
    options = nodes_dict[state]
    state = nodes_dict[state][1 if dir == 'R' else 0]

print(steps)

