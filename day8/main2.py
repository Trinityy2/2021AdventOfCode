file = open("input.txt")

def get_data(line):
    line = line.strip('\n').split(' | ')
    # we have 2 here. First one is pattern:
    patterns = line[0]
    patterns = patterns.split(' ')
    outputs = line[1]
    outputs = outputs.split(' ')
    return patterns, outputs

def get_from_length(enc_numbers, pattern):
    pattern = ''.join(sorted([x for x in pattern]))
    # Get based on the length of the numbers
    if len(pattern) == 2:
        enc_numbers[pattern] = 1
    elif len(pattern) == 4:
        enc_numbers[pattern] = 4
        print(enc_numbers)
    elif len(pattern) == 3:
        enc_numbers[pattern] = 7
    elif len(pattern) == 7:
        enc_numbers[pattern] = 8

def get_encoded(enc_numbers, patterns):
    # For question 1 we're only finding 1, 4, 7, 8
    for pattern in patterns:
        if len(pattern) in [2,4,3,7]:
            get_from_length(enc_numbers, pattern)


counter = 0
for line in file:
    # We're going to process each one by line
    patterns, outputs = get_data(line)
    enc_numbers = {} # Where we'll store our encoded numbers
    get_encoded(enc_numbers, patterns)

    # Now lets just check for the obvious numbers
    for output in outputs:
        output = ''.join(sorted([x for x in output]))
        if enc_numbers.get(output, False):
            counter += 1

print(counter)