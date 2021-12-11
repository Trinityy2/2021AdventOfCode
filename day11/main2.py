from typing import List


file = open('input.txt')

dumbopus = []

for line in file:
    line = line.strip('\n')
    dumbopus.append([int(x) for x in line])


def incrementAll(dumbopus, row, col):
    # Increments all around the given row, col, starting from top left
    for rmodifier in [-1, 0, 1]:
        if row + rmodifier >= 0 and row + rmodifier < len(dumbopus):
            for cmodifier in [-1, 0, 1]:
                if col + cmodifier >= 0 and col + cmodifier < len(dumbopus[0]):
                    if not isinstance(dumbopus[row+rmodifier][col+cmodifier], List):
                        dumbopus[row + rmodifier][col + cmodifier] += 1


def checkFlash(dumbopus, row, col):
    # If we dont flash, we can just return
    if row < 0 or col < 0 or row >= len(dumbopus) or col >= len(dumbopus[row]):
        # Doesn't exist
        return
    elif isinstance(dumbopus[row][col], List):
        return
    if dumbopus[row][col] <= 9:
        return
    else:
        # Here we have to start rippling by checking up, down, left, right
        dumbopus[row][col] = ["Flashed"]
        incrementAll(dumbopus, row, col)
        checkFlash(dumbopus, row-1, col)
        checkFlash(dumbopus, row+1, col)
        checkFlash(dumbopus, row, col-1)
        checkFlash(dumbopus, row, col+1)

        # Make sure to do diagonals too (top right, top left, bottom right, bottom left)
        checkFlash(dumbopus, row-1, col-1)
        checkFlash(dumbopus, row-1, col+1)
        checkFlash(dumbopus, row+1, col-1)
        checkFlash(dumbopus, row+1, col+1)


def resetToZero(dumbopus):
    score = 0
    for row in range(len(dumbopus)):
        for col in range(len(dumbopus[0])):
            if isinstance(dumbopus[row][col], List):
                dumbopus[row][col] = 0
                score += 1
    return False if score != len(dumbopus) * len(dumbopus[0]) else True


def step(dumbopus):
    for row in range(len(dumbopus)):
        for col in range(len(dumbopus)):
            if isinstance(dumbopus[row][col], int):
                dumbopus[row][col] += 1
                checkFlash(dumbopus, row, col)
    return resetToZero(dumbopus)


# for line in dumbopus:
#     print(line)
# print('')

timer = 0
while True:
    timer += 1
    if step(dumbopus):
        break

print(timer)
