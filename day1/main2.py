file = open("input.txt")

counter = 0
current_four = []

for line in file:
    if len(current_four) != 3:
        current_four.append(int(line))
    
    else:
        current_four.append(int(line))
        # increment counter
        if sum(current_four[0:3]) < sum(current_four[1:4]):
            counter += 1
        current_four.pop(0)

print(counter)
