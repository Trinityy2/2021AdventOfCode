file = open('input.txt')

fishinput = None
for line in file:
    fishinput = line.strip().split(',')
    break

size_timer = [0,0,0,0,0,0,0,0,0] # 9 zeroes representing the 9 days
for fish in fishinput:
    size_timer[int(fish)] += 1


def left_shift(size_timer):
    temp = []
    for i in size_timer[1:]:
        temp.append(i)
    
    temp[6] += size_timer[0]
    temp.append(size_timer[0])
    return temp

print(size_timer)

no_of_days = 256
for day in range(no_of_days):
    size_timer = left_shift(size_timer)
    print(size_timer)

print(sum(size_timer))