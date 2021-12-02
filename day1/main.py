file = open("input.txt")

counter = 0
last_number = 0

for line in file:
    if last_number != 0:
        if int(line) > last_number:
            counter += 1
    
    last_number = int(line)

print(counter)