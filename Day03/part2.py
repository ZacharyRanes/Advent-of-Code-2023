input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

part_locations = []

for i, line in enumerate(input_array):
    for j, c in enumerate(line):
        if c == "*":
            part_locations.append((i,j))

for i, j in part_locations:
    number_location = []

    if input_array[i-1][j-1].isdigit():
        number_location.append((i-1,j-1))
    if input_array[i][j-1].isdigit():
        number_location.append((i,j-1))
    if input_array[i+1][j-1].isdigit():
        number_location.append((i+1,j-1))

    if input_array[i-1][j].isdigit():
        number_location.append((i-1,j))
    if input_array[i+1][j].isdigit():
        number_location.append((i+1,j))

    if input_array[i-1][j+1].isdigit():
        number_location.append((i-1,j+1))
    if input_array[i][j+1].isdigit():
        number_location.append((i,j+1))
    if input_array[i+1][j+1].isdigit():
        number_location.append((i+1,j+1))

    part_numbers = []

    for i, j in number_location:
        line = input_array[i]
        jl = j
        jr = j
        while line[jr + 1].isdigit():
            jr += 1
        while line[jl - 1].isdigit():
            jl -= 1
        if (i,jl,jr+1) not in part_numbers:
            part_numbers.append((i,jl,jr+1))

    if len(part_numbers) == 2:
        total += int(input_array[part_numbers[0][0]][part_numbers[0][1]:part_numbers[0][2]]) * int(input_array[part_numbers[1][0]][part_numbers[1][1]:part_numbers[1][2]])
print(total)