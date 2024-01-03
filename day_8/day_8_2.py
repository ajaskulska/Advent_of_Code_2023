from math import lcm


with open('input_day8.txt', 'r') as file:
    input = [line.strip() for line in file]

instructions = [i for i in input[0]]
nodes = input[2:]
nodes_dict = {}
for n in nodes:
    curr = n.replace("= (", " ").replace(", ", " ").replace(")", " ").split()
    nodes_dict[curr[0]] = [curr[1], curr[2]]

state = [n for n in nodes_dict if n[-1] == 'A']
steps = 0
steps_by_node = []
for s in state:
    while s[-1] != 'Z': 
        dir = instructions[steps % len(instructions)]
        steps += 1
        options = nodes_dict[s]
        if dir == 'L':
            s = options[0]
        else:
            s = options[1]

    steps_by_node.append(steps)
    steps = 0

print(lcm(*steps_by_node))





