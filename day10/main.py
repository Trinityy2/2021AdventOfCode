match = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137)
}

file = open('input.txt')


def findcorrupted(line):
    stack = []
    for char in line:
        if char in match.keys():
            # If stack is empty, then autofail
            if not len(stack):
                return match[char][1]
            elif stack[-1] != match[char][0]:
                return match[char][1]
            else:
                stack.pop()
        else:
            # Its opening
            stack.append(char)
    return 0


score = 0
for line in file:
    line = line.strip('\n')
    score += findcorrupted(line)

print(score)