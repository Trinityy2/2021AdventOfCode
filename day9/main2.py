file = open('input.txt')

themap = []
for line in file:
    line = line.strip('\n')
    themap.append([0 if x != '9' else -1 for x in line])


def determine_basin_size(themap, row, col, top3):
    counter = _determine_basin_size(themap, row, col)
    top3.append(counter)
    top3.sort()
    if len(top3) == 4:
        top3.pop(0)


def _determine_basin_size(themap, row, col):
    counter = 0
    # fail if we're at the edges
    if row < 0 or row >= len(themap) or col < 0 or col >= len(themap[0]):
        return counter
    # Check current
    elif themap[row][col] != 0:
        return counter
    else:
        # Since we are still in the basin, keep going up, down, left, right
        themap[row][col] = 1
        counter += 1

        counter += _determine_basin_size(themap, row-1, col)    # up
        counter += _determine_basin_size(themap, row+1, col)    # down
        counter += _determine_basin_size(themap, row, col-1)    # left
        counter += _determine_basin_size(themap, row, col+1)    # right

        return counter


# Now that we have the map, we go through each one and traverse, modifying the map once we've
# accounted for it
top3 = []
for row in range(len(themap)):
    for col in range(len(themap[0])):
        if themap[row][col] == 0:
            determine_basin_size(themap, row, col, top3)

print(top3)
print(top3[0]*top3[1]*top3[2])
