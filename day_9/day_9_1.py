with open('input_day9.txt', 'r') as file:
    input = [line.strip() for line in file]

total = 0
for line in input:
    seq = [int(l) for l in line.split()]
    last_el = [seq[-1]]

    while len(set(seq)) != 1:
        seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        last_el.append(seq[-1])

    total += sum(last_el)

print(total)

