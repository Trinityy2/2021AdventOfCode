def binary_calculate(binary):
    # To find the binary
    res = 0
    current_value = 1
    for x in range(len(binary)-1, -1, -1):
        if binary[x]:
            res += current_value
        current_value += current_value

    return res

file = open("input.txt")

line_count = 0
length_of_binary = 12
current_sum = [0]*length_of_binary

for line in file:
    line = line.strip("\n")
    line_count += 1
    for i in range(len(line)):
        current_sum[i] += int(line[i])

# Now we divide by two. This gives us gamma
line_count_half = line_count/2
final_binary = [0]*length_of_binary

for col in range(length_of_binary):
    final_binary[col] = 0 if current_sum[col] < line_count_half else 1

# gamma rate
gamma_rate = binary_calculate(final_binary)
# epsilon rate is the last 5
epsilon_rate = binary_calculate([0 if x else 1 for x in final_binary])

print(gamma_rate, epsilon_rate)
print(gamma_rate * epsilon_rate)