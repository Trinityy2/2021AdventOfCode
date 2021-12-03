from copy import deepcopy

def find_common(list, co2=False):
    length_of_binary = len(list[0])
    current_sum = [0] * length_of_binary
    
    for item in list:
        for i in range(len(item)):
            current_sum[i] += int(item[i])

    # Now we divide by two. This gives us the common binary
    line_count_half = len(list)/2
    final_binary = [0]*length_of_binary

    for col in range(length_of_binary):
        if not co2:
            final_binary[col] = 0 if current_sum[col] < line_count_half else 1
        else:
            if not (current_sum[col] != 0 or current_sum[col] == len(list)):
                final_binary[col] = 0 if current_sum[col] <= line_count_half else 1
            else:
                current_sum[col] = 0 if current_sum[col] != 0 else 1

    return final_binary

def binary_calculate(binary):
    # To find the binary
    res = 0
    current_value = 1
    for x in range(len(binary)-1, -1, -1):
        if int(binary[x]):
            res += current_value
        current_value += current_value

    return res

def get_split(list, search_term, position):
    # list is already sorted in ascending order
    # print(f'list: {list}, search: {search_term}, pos: {position}')
    direction = None
    dir_range = None
    # print(f"search term pos: {search_term[position]}")
    if int(search_term[position]) == 0:
        # print("up")
        #start from top
        dir_range = range(0, len(list))
        direction = "up"
    else:
        # print('down')
        dir_range = range(len(list)-1, 0, -1)
        direction = "down"

    list_pos = 0
    for i in dir_range:
        if int(list[i][position]) != int(search_term[position]):
            list_pos = i
            break

    # This extra conditional is here because we might accidentally have gotten the least common wrong
    result = list[:list_pos] if direction == 'up' else list[list_pos + 1:]
    # if result:
    #     return result
    # else:
    #     return list
    return result

file = open("input.txt")
all_values = []

for line in file:
    line = line.strip("\n")
    all_values.append(line)

common_binary = find_common(all_values)
uncommon_binary = [0 if x else 1 for x in common_binary]

# To find the oxygen generator rating:
list_copy = sorted(deepcopy(all_values))

pos = 0
while len(list_copy) != 1:
    list_copy = get_split(list_copy, find_common(list_copy), pos)
    pos += 1

o2 = binary_calculate(list_copy[0])
print(o2)

# To find the co2 scrubber rating:
list_copy = sorted(deepcopy(all_values))

pos = 0
while len(list_copy) != 1:
    flipped = [0 if int(x) else 1 for x in find_common(list_copy, co2=True)]
    list_copy = get_split(list_copy, flipped, pos)
    pos += 1

co2 = binary_calculate(list_copy[0])
print(co2)
print(o2*co2)