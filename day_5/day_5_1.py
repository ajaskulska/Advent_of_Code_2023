with open('input_day5.txt', 'r') as file:
    input = [line.strip() for line in file]

sub_input = [[]]

for item in input:
    if item == "":
        sub_input.append([])
    else:
        sub_input[-1].append(item)
        
seeds = [s.split(" ") for s in sub_input[0]][0][1:]     
seed_to_soil = sub_input[1][1:]
soil_to_fertilizer = sub_input[2][1:]
fertilizer_to_water = sub_input[3][1:]
water_to_light = sub_input[4][1:]
light_to_temp = sub_input[5][1:]
temp_to_humid = sub_input[6][1:]
humid_to_loc = sub_input[7][1:]

def find_next_dest(sub_data, next_source):
    counter = 0
    next_dest = []

    for line in sub_data:
        counter += 1

        line = line.split(" ")
        ran = int(line[2])
        dest = int(line[0])
        source = int(line[1])

        for s in next_source:
            s = int(s)
            if s >= source and s <= source+(ran-1):
                diff = s - source
                dest_diff = dest + diff
                next_dest.append(dest_diff)
                
    return next_dest


find_soil = find_next_dest(seed_to_soil, seeds)
find_fertilizer = find_next_dest(soil_to_fertilizer, find_soil)
find_water = find_next_dest(fertilizer_to_water, find_fertilizer)
find_light = find_next_dest(water_to_light, find_water)
find_temp = find_next_dest(light_to_temp, find_light)
find_humid = find_next_dest(temp_to_humid, find_temp)
find_location = find_next_dest(humid_to_loc, find_humid)

print(min(find_location))