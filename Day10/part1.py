class Pipe:
    top_open = False
    left_open = False
    right_open = False
    bottom_open = False

    def __init__(self, top_open, left_open, right_open, bottom_open):
        self.top_open = top_open
        self.left_open = left_open
        self.right_open = right_open
        self.bottom_open = bottom_open


def main():
    total = 0
    input_array = []

    with open('input_test', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    sketch = []
    start = ()

    for i, line in enumerate(input_array):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
                sketch.append(Pipe(True, True, True, True))
            if c == ".":
                sketch.append(None)

    print(start)
    print(sketch)

    return total


if __name__ == "__main__":
    print(main())
