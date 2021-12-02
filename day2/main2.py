posx = 0 # Distance
posy = 0 # Depth
aim = 0

file = open('input.txt')

for line in file:
    movement = line.split()
    if movement[0] == 'forward':
        posx += int(movement[1])
        posy += aim * int(movement[1])
    elif movement[0] == "up":
        aim -= int(movement[1])
    elif movement[0] == "down":
        aim += int(movement[1])

print(posx*posy)