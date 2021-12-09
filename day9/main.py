file = open('input.txt')

length = None
entirelist = ''

for line in file:
    line = line.strip('\n')
    if not length:
        length = len(line)
    entirelist = entirelist + line

entirelist = [int(x) for x in entirelist]


def check_if_low(entirelist, curr, length):
    curr_pos = curr % length
    # check up and left:
    if curr-1 >= 0 and curr_pos != 0.0:
        if entirelist[curr] >= entirelist[curr-1]:
            return False
    if curr-length >= 0:
        if entirelist[curr] >= entirelist[curr-length]:
            return False

    # check right and down:
    if curr+1 < len(entirelist) and curr_pos != (length-1):
        if entirelist[curr] >= entirelist[curr+1]:
            return False
    if curr+length < len(entirelist):
        if entirelist[curr] >= entirelist[curr+length]:
            return False
    return True


risk = 0
counter = [0]
for x in range(0, len(entirelist)):
    if check_if_low(entirelist, x, length):
        risk += (entirelist[x] + 1)

print(risk)