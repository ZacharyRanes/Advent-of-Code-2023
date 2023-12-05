input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

seeds = list(map(int, input_array[0].split()[1:]))

index = 3

levels = []

while True:

    mapped = []

    while input_array[index][0].isdigit():
        work = list(map(int, input_array[index].split()))
        mapped.append((work[1], work[1]+work[2], work[0]-work[1]))

        index += 1
        if index >= len(input_array):
            break

    levels.append(mapped)

    index += 2

    if index >= len(input_array):
        break


for level in levels:
    path = []
    for s in seeds:
        found = False
        print(level)
        for m in level:
            if s >= m[0] and s <= m[1]:
                path.append(s + m[2])
                found = True
                break
        if not found:
            path.append(s)

    seeds = path

print(min(seeds))
