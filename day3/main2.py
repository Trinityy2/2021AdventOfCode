def binary_calculate(binary):
    # To find the binary
    res = 0
    current_value = 1
    for x in range(len(binary)-1, -1, -1):
        if binary[x]:
            res += current_value
        current_value += current_value

    return res

file = open("testinput.txt")

line_count = 0
length_of_binary = 5
current_sum = [0]*length_of_binary
all_values = []

for line in file:
    line = line.strip("\n")
    all_values.append(line)
    line_count += 1
    for i in range(len(line)):
        current_sum[i] += int(line[i])

# Now we divide by two. This gives us most common
line_count_half = line_count/2
common_binary = [0]*length_of_binary

for col in range(length_of_binary):
    common_binary[col] = 0 if current_sum[col] < line_count_half else 1

# To find this we can sort and filter
common_binary_str = [str(x) for x in common_binary]
common_binary_str = ''.join(common_binary_str)
print(f"common binary string: {common_binary_str}")
if common_binary_str[0] == 0:
    all_values = sorted(all_values)
else: 
    all_values = sorted(all_values, reverse=True)

o2generator_rating = 0
curr = 1
for x in range(len(all_values)):
    if common_binary_str[0:curr] in all_values[x][0:curr]:
        if common_binary_str[0:curr] in all_values[x+1][0:curr]:
            curr += 1
        else:
            o2generator_rating = binary_calculate(all_values[x])

print(o2generator_rating)

# Do the same for uncommon binary
uncommon_binary_str = ['0' if x else '1' for x in common_binary]
uncommon_binary_str = ''.join(uncommon_binary_str)
print(f"uncommon binary string: {uncommon_binary_str}")
if uncommon_binary_str[0] == 0:
    all_values = sorted(all_values)
else:
    all_values = sorted(all_values, reverse=True)

co2scrubber_rating = 0
curr = 1
for x in range(len(all_values)):
    if uncommon_binary_str[0:curr] in all_values[x][0:curr]:
        if uncommon_binary_str[0:curr] in all_values[x+1][0:curr]:
            curr += 1
        else:
            co2scrubber_rating = binary_calculate(all_values[x])

print(co2scrubber_rating * o2generator_rating)
