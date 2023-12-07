def main():
    input_array = []

    with open('input_test', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    data = []

    for line in input_array:
        data.append((line.split()[0],int(line.split()[1])))

    # print(data)

    print(compare_hands(data[0][0], data[1][0]))


def compare_hands(h1:str, h2:str) -> bool:
    """
    given two camel cards hands as strings
    returns:
        True if h1 >= h2
        False if h1 < h2
    """
    h1level = hand_level(h1)
    h2level = hand_level(h2)

    if h1level > h2level:
        return True
    if h1level < h2level:
        return False
    if h1level == h2level:
        for i in range(5):
            if card_str(h1[i]) > card_str(h2[i]):
                return True
            if card_str(h1[i]) < card_str(h2[i]):
                return False

def hand_level(h:str) -> int:
    # 5 of a kind
    if h.count(h[0]) == 5:
        return 7
    # 4 of a kind
    if h.count(h[0]) == 4 or h.count(h[1]) == 4:
        return 6
    # Full house / Three of a kind
    if h.count(h[0]) == 3 or h.count(h[1]) == 3 or h.count(h[2]) == 3:
        pass

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