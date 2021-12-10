match = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137)
}

autocomplete = {
    '(': (')', 1),
    '[': (']', 2),
    '{': ('}', 3),
    '<': ('>', 4)
}

file = open('input.txt')


def finderrors(line):
    stack = []
    for char in line:
        # First check if its corrupted
        if char in match.keys():
            # If stack is empty, then autofail
            if not len(stack):
                return 0
            elif stack[-1] != match[char][0]:
                return 0
            else:
                stack.pop()
        else:
            # Its opening
            stack.append(char)

    # At this stage, we can find out if its incomplete
    if len(stack) > 0:
        # Now we autocomplete and get a score
        stack.reverse()
        result = [autocomplete[x][1] for x in stack]
        score = 0
        for x in result:
            score = score * 5
            score += x
            print(score, x)
        return score
    return 0


scores = []
for line in file:
    line = line.strip('\n')
    score = finderrors(line)
    if score > 0:
        scores.append(score)

scores.sort()
print(scores[(len(scores) // 2)])