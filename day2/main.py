posx = 0 # Distance
posy = 0 # Depth

file = open('input.txt')

for line in file:
    movement = line.split()
    if movement[0] == 'forward':
        posx += int(movement[1])
    elif movement[0] == "up":
        posy -= int(movement[1])
    elif movement[0] == "down":
        posy += int(movement[1])

print(posx*posy)