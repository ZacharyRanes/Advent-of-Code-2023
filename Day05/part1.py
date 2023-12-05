input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

seeds = list(map(int, input_array[0].split()[1:]))

index = 3

levels = []

while True:

    mapped = {}

    while input_array[index][0].isdigit():
        work = list(map(int, input_array[index].split()))
        for i in range(work[2]):
            mapped[work[1]+i] = work[0]+i

        index += 1
        if index >= len(input_array):
            break

    # levels.append(mapped)

    print(mapped)

    index += 2

    if index >= len(input_array):
        break

# for level in levels:
#     path = []
#     for s in seeds:
#         if s in level:
#             path.append(level[s])
#         else:
#             path.append(s)
#     seeds = path

# print(min(seeds))
