input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

max_red = 12
max_green = 13
max_blue = 14

total = 0

for line in input_array:
    game_id = int(line.split(":")[0].split(" ")[1])
    total += game_id

    # print("Game:", game_id)

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
        # print(seen)
        if seen["red"] > max_red or seen["green"] > max_green or seen["blue"] > max_blue:
            total -= game_id
            break

    # print(total)

print(total)
