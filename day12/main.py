from copy import deepcopy

file = open("input.txt")

paths = {}
for line in file:
    line = line.strip('\n').split('-')
    if not paths.get(line[0], False):
        paths[line[0]] = [line[1]]
    else:
        paths[line[0]].append(line[1])

    # Do it in reverse too
    if not paths.get(line[1], False):
        paths[line[1]] = [line[0]]
    else:
        paths[line[1]].append(line[0])


def _find_paths(paths, possible_paths, curr_path, next_path: str):
    """ Next path is just a string of the key to the next path we're trying out """
    # If the next_path is string, if it already exists, then we dont allow it
    if next_path == 'start':
        if 'start' in curr_path:
            return
    elif next_path == 'end':
        # We made it to the end and we should record this as a possible path
        curr_path.append('end')
        possible_paths.append(deepcopy(curr_path))
        curr_path.pop(-1)
        return
    else:
        # Some additional logic for if we're not at the end
        if next_path.islower():
            # Can only traverse once
            if next_path in curr_path:
                return

    # If we reach this part, it means we can start doing the rest
    curr_path.append(next_path)
    for check_path in paths[next_path]:
        _find_paths(paths, possible_paths, curr_path, check_path)
    curr_path.pop(-1)


def find_paths(paths, possible_paths):
    curr_path = []
    # We always start at start here
    _find_paths(paths, possible_paths, curr_path, 'start')


# Now we can try to find the paths recursively
possible_paths = []
find_paths(paths, possible_paths)
for item in possible_paths:
    print(item)
print(len(possible_paths))