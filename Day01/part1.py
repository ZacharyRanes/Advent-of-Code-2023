input_array = []

with open('input1', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

for line in input_array:

    for c in line:
        if c.isdigit():
            d1 = c

    for c in reversed(line):
        if c.isdigit():
            d2 = c

    total += int(d2 + d1)

print(total)
