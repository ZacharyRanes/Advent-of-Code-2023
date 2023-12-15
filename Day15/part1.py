def main():
    total = 0

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_data = file_name.readline()

    puzzles = input_data.strip().split(",")

    for p in puzzles:
        total += my_hash(p)

    return total


def my_hash(p: str) -> int:
    current_value = 0
    for c in p:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


if __name__ == "__main__":
    print(main())
