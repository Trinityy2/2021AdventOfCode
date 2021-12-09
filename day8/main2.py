file = open("input.txt")

def get_data(line):
    line = line.strip('\n').split(' | ')
    # we have 2 here. First one is pattern:
    patterns = line[0]
    patterns = patterns.split(' ')
    outputs = line[1]
    outputs = outputs.split(' ')
    return patterns, outputs

def get_from_length(enc_numbers, easy_numbers, pattern):
    pattern = ''.join(sorted([x for x in pattern]))
    # Get based on the length of the numbers
    if len(pattern) == 2:
        enc_numbers[pattern] = 1
        easy_numbers[1] = pattern
    elif len(pattern) == 4:
        enc_numbers[pattern] = 4
        easy_numbers[4] = pattern

    elif len(pattern) == 3:
        enc_numbers[pattern] = 7
        easy_numbers[7] = pattern

    elif len(pattern) == 7:
        enc_numbers[pattern] = 8
        easy_numbers[8] = pattern

def get_complex_numbers(enc_numbers, easy_numbers, pattern):
    # These are for more complex numbers
    patternset = set(pattern)
    pattern = ''.join(sorted([x for x in pattern]))
    if len(pattern) == 5:
        # Either 2, 3 or 5
        oneset = set(easy_numbers[1])
        fourset = set(easy_numbers[4])
        onefourinverse = fourset - oneset.intersection(fourset)
        if len(oneset.intersection(patternset)) == 2:
            enc_numbers[pattern] = 3
        elif len(onefourinverse.intersection(patternset)) == 2:
            enc_numbers[pattern] = 5
        else: enc_numbers[pattern] = 2
    else:
        # pattern length is 6, meaning its either 0, 6 or 9
        fourset = set(easy_numbers[4])
        sevenset = set(easy_numbers[7])
        if len(fourset.intersection(patternset)) == 4:
            enc_numbers[pattern] = 9
        elif len(sevenset.intersection(patternset)) == 2:
            enc_numbers[pattern] = 6
        else:
            enc_numbers[pattern] = 0

def get_encoded(enc_numbers, patterns):
    # For question 1 we're only finding 1, 4, 7, 8
    # Just to keep the reverse for the definitive ones, we can make a reverse one too
    easy_numbers = {}
    complex_numbers = []
    for pattern in patterns:
        if len(pattern) in [2,4,3,7]:
            get_from_length(enc_numbers, easy_numbers, pattern)
        else:
            # # Keep these for later as we got to figure out the obvious ones first
            # if len(pattern) == 5:
            #     complex_numbers[5].append(pattern)
            # else:
            #     #len of 6:
            #     complex_numbers[6].append(pattern)
            complex_numbers.append(pattern)
                
    # Now we can do the rest of the complex numbers
    for pattern in complex_numbers:
        get_complex_numbers(enc_numbers, easy_numbers, pattern)

numbers = []
for line in file:
    # We're going to process each one by line
    patterns, outputs = get_data(line)
    enc_numbers = {} # Where we'll store our encoded numbers
    get_encoded(enc_numbers, patterns)

    # Now lets just check for the obvious numbers
    print(enc_numbers)
    numlist = []
    for output in outputs:
        output = ''.join(sorted([x for x in output]))
        numlist.append(str(enc_numbers[output]))
    numbers.append(int(''.join(numlist)))


print(sum(numbers))