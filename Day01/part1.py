input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

for line in input_array:

    for c in line:
        if c.isdigit():
            d1 = c
            break

    for c in reversed(line):
        if c.isdigit():
            d2 = c
            break

    total += int(d1 + d2)

print(total)
