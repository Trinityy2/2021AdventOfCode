file = open('input.txt')

crabs = []
for line in file:
    line = line.strip('\n').split(',')
    for num in line:
        crabs.append(int(num))
    break

possible_positions = sorted(crabs)
minimum = None

for pos in range(possible_positions[0], possible_positions[-1]+1):
    res_sum = 0
    for crab_dist in crabs:
        temp = (0.5*abs(crab_dist-pos)) * (abs(crab_dist-pos)+1)
        res_sum += temp
    swap = True if not minimum or res_sum < minimum else False
    minimum = res_sum if swap else minimum

print(minimum)