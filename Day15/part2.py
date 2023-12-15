def main():
    total = 0

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_data = file_name.readline()

    puzzles = input_data.strip().split(",")

    boxes = [list() for x in range(256)]

    for p in puzzles:
        if "=" in p:
            k = "".join([p.split("=")[0]])
            hash_value = my_hash(k)
            v = int(p.split("=")[1])
            boxes[hash_value] = check_add((k, v), boxes[hash_value])
        elif "-" in p:
            k = "".join([p.split("-")[0]])
            hash_value = my_hash(k)
            boxes[hash_value] = check_remove(k, boxes[hash_value])
        else:
            print("error")

    print(boxes)
    for i, b in enumerate(boxes):
        for j, s in enumerate(b):
            total += ((i+1) * (j+1) * (s[1]))

    return total


def check_add(v: tuple, l: list) -> list:
    for i, t in enumerate(l):
        if t[0] == v[0]:
            l[i] = v
            return l
    l.append(v)
    return l


def check_remove(k: str, l: list) -> list:
    for i, t in enumerate(l):
        if t[0] == k:
            del l[i]
    return l


def my_hash(p: str) -> int:
    current_value = 0
    for c in p:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


if __name__ == "__main__":
    print(main())
    # 30465
