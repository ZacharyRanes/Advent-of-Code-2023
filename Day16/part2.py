from collections import deque


def main():

    puzzle = []

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

        # Turn the puzzle input to 2D list
        puzzle = [list(x[:-1]) for x in input_array]

    most_e = 0

    for i, l in enumerate(puzzle):
        most_e = max(most_e, e_check(puzzle, (i, 0, 1)))
        most_e = max(most_e, e_check(puzzle, (i, len(l), 3)))

    for i, l in enumerate(puzzle[0]):
        most_e = max(most_e, e_check(puzzle, (0, i, 4)))
        most_e = max(most_e, e_check(puzzle, (len(puzzle), i, 2)))

    return most_e


def e_check(puzzle: list[list[str]], start: tuple) -> int:
    total = 0

    # 2D list same demotions as the puzzle with all values set to false
    energized = [["." for x in range(len(puzzle[0]))]
                 for x in range(len(puzzle))]

    beams = deque()
    past = []

    # Beam tuple
    # (i, j , d)
    # d being directions as int
    # -> 1
    # /\ 2
    # <- 3
    # \/ 4

    beams.append(start)

    # deque evaluates to false when empty
    while beams:
        b = beams.pop()
        if b not in past and \
           b[0] < len(puzzle) and b[0] >= 0 and \
           b[1] < len(puzzle[0]) and b[1] >= 0:

            energized[b[0]][b[1]] = "#"

            if puzzle[b[0]][b[1]] == ".":
                if b[2] == 1:
                    beams.append((b[0], b[1]+1, 1))
                elif b[2] == 2:
                    beams.append((b[0]-1, b[1], 2))
                elif b[2] == 3:
                    beams.append((b[0], b[1]-1, 3))
                elif b[2] == 4:
                    beams.append((b[0]+1, b[1], 4))

            elif puzzle[b[0]][b[1]] == "/":
                if b[2] == 1:
                    beams.append((b[0]-1, b[1], 2))
                elif b[2] == 2:
                    beams.append((b[0], b[1]+1, 1))
                elif b[2] == 3:
                    beams.append((b[0]+1, b[1], 4))
                elif b[2] == 4:
                    beams.append((b[0], b[1]-1, 3))

            elif puzzle[b[0]][b[1]] == "\\":
                if b[2] == 1:
                    beams.append((b[0]+1, b[1], 4))
                elif b[2] == 2:
                    beams.append((b[0], b[1]-1, 3))
                elif b[2] == 3:
                    beams.append((b[0]-1, b[1], 2))
                elif b[2] == 4:
                    beams.append((b[0], b[1]+1, 1))

            elif puzzle[b[0]][b[1]] == "|":
                if b[2] == 1:
                    beams.append((b[0]-1, b[1], 2))
                    beams.append((b[0]+1, b[1], 4))
                elif b[2] == 2:
                    beams.append((b[0]-1, b[1], 2))
                elif b[2] == 3:
                    beams.append((b[0]-1, b[1], 2))
                    beams.append((b[0]+1, b[1], 4))
                elif b[2] == 4:
                    beams.append((b[0]+1, b[1], 4))

            elif puzzle[b[0]][b[1]] == "-":
                if b[2] == 1:
                    beams.append((b[0], b[1]+1, 1))
                elif b[2] == 2:
                    beams.append((b[0], b[1]+1, 1))
                    beams.append((b[0], b[1]-1, 3))
                elif b[2] == 3:
                    beams.append((b[0], b[1]-1, 3))
                elif b[2] == 4:
                    beams.append((b[0], b[1]+1, 1))
                    beams.append((b[0], b[1]-1, 3))

            # prevent infante loops in the beam
            past.append(b)

    for line in energized:
        # print(line)
        for e in line:
            if e == "#":
                total += 1

    return total


if __name__ == "__main__":
    print(main())
