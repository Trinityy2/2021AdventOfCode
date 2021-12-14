file = open('input.txt')

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
for x in range(len(template)-1):
    polymer_count[template[x:x+2]] += 1
    no_of_letter[template[x]] += 1
    if x == len(template) - 2:  # Just to count that last letter too
        no_of_letter[template[x+1]] += 1

# By now we'll have our counts of everything, so we can start adding and modifying
no_of_steps = 40
for i in range(no_of_steps):
    to_add = []
    for key, value in polymer_count.items():
        if value:
            # print(i, key, value)
            # if we have this polymer, we subtract that polymer, and add two new polymers
            letter_to_add = polymer[key]
            to_add.append((key[0]+polymer[key], value))
            to_add.append((polymer[key]+key[1], value))
            no_of_letter[polymer[key]] += 1 * value
            polymer_count[key] = 0

    for key, value in to_add:
        polymer_count[key] += value

counts = sorted(no_of_letter.values())
print(counts[-1] - counts[0])
