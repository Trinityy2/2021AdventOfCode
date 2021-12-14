file = open('testinput.txt')

template = None
polymer = {}
polymer_count = {}
no_of_letter = {}

for line in file:
    line = line.strip('\n')
    if '->' not in line and len(line) != 0:
        template = line
    elif '->' in line:
        line = line.split(' -> ')
        polymer[line[0]] = line[1]
        polymer_count[line[0]] = 0
        for letter in line[0]:
            if letter not in no_of_letter.keys():
                no_of_letter[letter] = 0

# Instead of template, we want to keep the count of each letter + polymer
print(template)
print(polymer)
print(polymer_count)
print(no_of_letter)