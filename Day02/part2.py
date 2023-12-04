input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

for line in input_array:
    needed_red = 0
    needed_green = 0
    needed_blue = 0

    # game_id = int(line.split(":")[0].split(" ")[1])

    game_data = line.split(":")[1].split(";")
    for r in game_data:
        seen = {
            "red":0,
            "green":0,
            "blue":0
        }
        moves = r.split(",")
        for p in moves:
            count, color = p.strip().split(" ")
            seen[color] += int(count)

        if seen["red"] > needed_red:
            needed_red = seen["red"]
        if seen["green"] > needed_green:
            needed_green = seen["green"]
        if seen["blue"] > needed_blue:
            needed_blue = seen["blue"]

    power = needed_red * needed_green * needed_blue
    total += power
print(total)