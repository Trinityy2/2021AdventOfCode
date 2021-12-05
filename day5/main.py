file = open('input.txt')
highestx = 0
highesty = 0

def set_highest(x: tuple, y:tuple):
    # Setting highestx and highesty for table creation later
    global highestx
    global highesty
    for i in (x, y):
        if highestx < i[0]:
            highestx = i[0]
        if highesty < i[1]:
            highesty = i[1]

def check_valid(x: tuple, y:tuple):
    # We want to ignore diagonals here
    if x[0] == y[0] or x[1] == y[1]:
        return True
    return False

coords = [] # Stores A and B (two coordinates) as a tuple in a dictionary
for line in file:
    line = line.split(' -> ')
    a = line[0].split(',')
    a = (int(a[0]), int(a[1]))
    b = line[1].split(',')
    b = (int(b[0]), int(b[1]))
    if check_valid(a, b):
        graph_line = {
            'a': a,
            'b': b
        }
        set_highest(a, b)
        coords.append(graph_line)

# Make graph
graph = [[0 for x in range(highestx+1)] for y in range(highesty+1)]

def customrange(start, stop):
    if start < stop:
        return range(start, stop+1)
    else:
        return range(stop, start+1)

# Draw lines
def draw(table, coorda, coordb):
    crange = None
    line = ''   # The axis in which it changes (not constant)
    if coorda[0] == coordb[0]:
        crange = customrange(coorda[1], coordb[1])
        line = 'y'
    else:
        crange = customrange(coorda[0], coordb[0])
        line = 'x'
    
    for i in crange:
        if line == 'y':
            table[i][coorda[0]] += 1
        else:
            table[coorda[1]][i] +=  1

for coord in coords:
    draw(graph, coord['a'], coord['b'])

# Get number of intersections here
intersection = 0
for y in range(highesty+1):
    for x in range(highestx+1):
        if graph[x][y] > 1:
            intersection += 1
print("score", intersection)

# print(draw(graph, coords[0]['a'], coords[0]['b']))
# for x in graph:
#     print(x)
    
