def main():
    total = 0
    input_array = []

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    position = ()

    for i, line in enumerate(input_array):
        for j, c in enumerate(line):
            if c == "S":
                position = (i, j)
    last = 0

    while True:
        total += 1

        if (position[0]-1) >= 0 and (input_array[position[0]-1][position[1]] in ["|", "7", "F", "S"]) and last != 1:
            position = (position[0]-1, position[1])
            last = 2

        elif (position[0]+1) < len(input_array) and (input_array[position[0]+1][position[1]] in ["|", "J", "L", "S"]) and last != 2:
            position = (position[0]+1, position[1])
            last = 1

        elif (position[1]-1) >= 0 and (input_array[position[0]][position[1]-1] in ["-", "L", "F", "S"]) and last != 3:
            position = (position[0], position[1]-1)
            last = 4

        elif (position[1]+1) < len(input_array[0]) and (input_array[position[0]][position[1]+1] in ["-", "7", "J", "S"]) and last != 4:
            position = (position[0], position[1]+1)
            last = 3

        if input_array[position[0]][position[1]] == "S":
            break

        print(position)
        
        if total > 1000:
            break

    return total


if __name__ == "__main__":
    print(main()/2)
