def main():
    total = 0

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_data = file_name.readline()

    puzzles = input_data.strip().split(",")

    for p in puzzles:
        current_value = 0
        for c in p:
            print
            current_value += ord(c)
            # print(current_value)
            current_value *= 17
            # print(current_value)
            current_value %= 256
            # print(current_value)
        total += current_value

    return total


if __name__ == "__main__":
    print(main())
