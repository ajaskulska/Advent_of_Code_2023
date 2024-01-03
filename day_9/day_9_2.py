with open('input_day9.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for line in input:
    seq = [int(l) for l in line.split()]
    first_el_list = [seq[0]]

    while len(set(seq)) != 1:
        seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        first_el_list.append(seq[0])

    result = 0
    new_first_el = 0
    for num in reversed(first_el_list):
        result = num - new_first_el
        new_first_el = result
    total += result

print(total)


