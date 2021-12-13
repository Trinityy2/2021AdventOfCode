file = open('testinput.txt')

folds = []
marks = []

for line in file:
    line = line.strip('\n')
    if line.startswith("fold"):
        line = line.split(' ')[2]
        folds.append((line.split('=')[0], int(line.split('=')[1])))
    elif len(line) != 0:
        line = line.split(',')
        marks.append((int(line[0]), int(line[1])))

print(folds)
print(marks)

def fold_along_x(marks, xaxis):
    # First to find the new size, we get the largest side
    
    for mark in marks:
        