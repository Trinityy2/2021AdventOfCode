file = open("input.txt")

def get_data(line):
    line = line.split(' | ')
    # we have 2 here. First one is pattern:
    pattern = line[0]
    pattern = pattern.split(' ')
    output = line[1]
    output = output.split(' ')
    return pattern, output

def get_from_length(pattern):
    # Get based on the length of the numbers
    pass

def get_encoded(enc_numbers, pattern):
    # For question 1 we're only finding 1, 4, 7, 8
    pass

for line in file:
    # We're going to process each one by line
    pattern, output = get_data(line)
    enc_numbers = {} # Where we'll store our encoded numbers
    get_encoded(enc_numbers, pattern)