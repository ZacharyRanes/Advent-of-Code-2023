def main():
    total = 0
    input_array = []

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    puzzle = []

    for line in input_array:
        if line.strip() == "":
            total += find_reflect(puzzle)
            puzzle = []
        else:
            puzzle.append(line.strip())

    return total


def find_reflect(puzzle: list[str]) -> int:
    for i in range(1, len(puzzle[0])):
        j = 0
        line = puzzle[j]
        while check_reflect(line[:i], line[i:]):
            j += 1
            if j >= len(puzzle):
                break
            line = puzzle[j]
        if j >= len(puzzle):
            return i

    for i in range(1, len(puzzle)):
        j = 0
        col = [x[j] for x in puzzle]
        while check_reflect(col[:i], col[i:]):
            j += 1
            if j >= len(puzzle[0]):
                break
            col = [x[j] for x in puzzle]
        if j >= len(puzzle[0]):
            return i * 100

    print("No Reflects")
    return 0


def check_reflect(left: str, right: str) -> bool:
    if len(left) > len(right):
        left = left[len(left)-len(right):]
    elif len(right) > len(left):
        right = right[:len(left)]

    return left == right[::-1]


if __name__ == "__main__":
    print(main())
