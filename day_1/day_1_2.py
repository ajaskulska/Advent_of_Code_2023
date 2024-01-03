with open('input_day1.txt', 'r') as file:
    input = [line.strip() for line in file]

to_find = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lengths = [len(s) for s in input]
longest_string = max(lengths)

twodigitlist = []

for line in input:
    left_ind = longest_string
    right_ind = 0
    newline = ''

    for n in to_find:
        target_first = line.find(n)
        target_last = line.rfind(n)
        twodigit = ''

        if target_first == -1:
            continue           
        if target_first <= left_ind:
            left_ind = target_first
            numb_ind = to_find.index(n)
            ldigit = str(numbers[numb_ind])
            
        if target_last == -1:
            continue
        if target_last >= right_ind:
            right_ind = target_last
            numb_ind = to_find.index(n)
            rdigit = str(numbers[numb_ind])
                
        twodigit += ldigit
        twodigit += rdigit
        newline = twodigit
    
    twodigitlist.append(newline)


print(sum(int(n) for n in twodigitlist))