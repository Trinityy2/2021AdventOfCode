file = open('input.txt')

crabs = []
for line in file:
    line = line.strip('\n').split(',')
    for num in line:
        crabs.append(int(num))
    break

possible_positions = list(set(crabs))

minimum = None
minimum_pos = None

for pos in possible_positions:
    res_sum = 0
    for crab_dist in crabs:
        temp = crab_dist - pos
        if temp < 0:
            res_sum -= temp
        else:
            res_sum += temp
    swap = True if not minimum or res_sum < minimum else False
    minimum = res_sum if swap else minimum
    minimum_pos = pos if swap else minimum_pos

print(minimum)