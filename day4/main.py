from copy import deepcopy

numbers = None
boards = []
the_input = []

file = open("input.txt")

for line in file:
    if ',' in line:
        the_input.append(line.strip('\n ').split(','))
    else:
        the_input.append(line.strip('\n ').split(' '))

for line in the_input:
    if not numbers:
        numbers = line
    else:
        if len(line) == 1:
            # We add a new board here
            boards.append([])
        else:
            # We are appending some numbers here
            # Some boards get messed up here. so we'll repair it
            if len(line) > 5:
                new_line = []
                for x in line:
                    if x != '':
                        new_line.append(x)
                boards[-1].append(new_line)
            else:
                boards[-1].append(line)

# We can add the answers here too for each board
marks = []
size = 5    # size of board
for x in range(len(boards)):
    # Make a board for each board
    mark_board = []
    for x in range(size):
        new_row = []
        for y in range(size):
            new_row.append(0)
        mark_board.append(new_row)
    marks.append(mark_board)
    
    # marks.append(mark_board)

def _check_board(board, mark, num):
    print("mark", mark)
    # Pass in the board and the mark. We'll mark it here
    for x in range(size):
        for y in range(size):
            if num == board[x][y]:
                mark[x][y] = 1
                # We found it so we can exit early
                print('markend', mark)
                return (x, y)
    
    # If we reached here, it wasn't on this board
    return None, None

complete = ['1']*5
def check_board(board, mark, num):
    row, column = _check_board(board, mark, num)
    found = False
    if row is not None:
        # If we found one, lets check that marked row and column
        # Lets check the row first
        print(mark[row])
        if sum(mark[row]) == size:
            found = True
        
        if not found:
            # Now we check column too
            if sum([int(_row[column]) for _row in mark]) == size:
                found = True

    return found

def get_result(board, mark, num):
    total = 0
    for x in range(size):
        for y in range(size):
            if not mark[x][y]:
                total += int(board[x][y])
    
    return total * int(num)

finished = False
counter = 0
for number in numbers:
    counter += 1
    print("counter", counter)
    for x in range(len(boards)):
        found = check_board(boards[x], marks[x], number)
        if found:
            print(get_result(boards[x], marks[x], number))
            finished = True
            break
    if finished:
        break