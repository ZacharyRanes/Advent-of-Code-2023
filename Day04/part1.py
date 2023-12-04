input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

for line in input_array:
    card = list(map(int, line.split("|")[0].split()[2:]))
    our = list(map(int, line.split("|")[1].split()))

    points = 0

    for n in card:
        if n in our:
            if points == 0:
                points = 1
            else:
                points *= 2
    total += points
print(total)