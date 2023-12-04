input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0
copy_pile = []


for i, line in enumerate(input_array):
    card = list(map(int, line.split("|")[0].split()[2:]))
    our = list(map(int, line.split("|")[1].split()))

    copy_pile.append([card,our,0])

for i, line in enumerate(copy_pile):

    for _ in range(line[2]+1):
        copy_index = 1
        for n in line[0]:
            if n in line[1]:
                copy_pile[i+copy_index][2] += 1
                copy_index += 1
        total += 1


print(total)