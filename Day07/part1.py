def main():
    input_array = []

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    data = []

    for line in input_array:
        data.append((line.split()[0],int(line.split()[1]),hand_level(line.split()[0])))

    # for i, h in enumerate(data):
    #     print(i+1, h)

    # bubble sort
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if compare_hands(data[j], data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break

    # for i, h in enumerate(data):
    #     print(i+1, h)

    total = 0
    for i, n in enumerate(data):
        bet = n[1]
        rank = int(i + 1)
        total += bet * rank
    print(total)


def compare_hands(h1:tuple, h2:tuple) -> bool:
    """
    given two camel cards hands as strings
    returns:
        True if h1 >= h2
        False if h1 < h2
    """

    if h1[2] > h2[2]:
        return True
    if h1[2] < h2[2]:
        return False
    if h1[2] == h2[2]:
        for i in range(5):
            if card_str(h1[0][i]) > card_str(h2[0][i]):
                return True
            if card_str(h1[0][i]) < card_str(h2[0][i]):
                return False

def hand_level(h:str) -> int:
    # 5 of a kind
    if h.count(h[0]) == 5:
        return 7
    # 4 of a kind
    if h.count(h[0]) == 4 or h.count(h[1]) == 4:
        return 6
    # Full house / Three of a kind
    if h.count(h[0]) == 3:
        sh = h.replace(h[0], "")
        if sh[0] == sh[1]:
            return 5
        else:
            return 4
    if h.count(h[1]) == 3:
        sh = h.replace(h[1], "")
        if sh[0] == sh[1]:
            return 5
        else:
            return 4
    if h.count(h[2]) == 3:
        sh = h.replace(h[2], "")
        if sh[0] == sh[1]:
            return 5
        else:
            return 4
    # Two pair / Onw pair
    if h.count(h[0]) == 2:
        sh = h.replace(h[0], "")
        if sh.count(sh[0]) == 2 or sh.count(sh[1]) == 2:
            return 3
        else:
            return 2
    if h.count(h[1]) == 2:
        sh = h.replace(h[1], "")
        if sh.count(sh[0]) == 2 or sh.count(sh[1]) == 2:
            return 3
        else:
            return 2
    if h.count(h[2]) == 2:
        sh = h.replace(h[2], "")
        if sh.count(sh[0]) == 2 or sh.count(sh[1]) == 2:
            return 3
        else:
            return 2
    if h.count(h[3]) == 2:
        sh = h.replace(h[3], "")
        if sh.count(sh[0]) == 2 or sh.count(sh[1]) == 2:
            return 3
        else:
            return 2
    # else High card
    return 1

def card_str(c:str) -> int:
    if c.isdigit():
        return int(c)
    if c == "T":
        return 10
    if c == "J":
        return 11
    if c == "Q":
        return 12
    if c == "K":
        return 13
    if c == "A":
        return 14

if __name__ == "__main__":
    main()