def main():
    total = 0
    input_array = []

    with open('input', 'r', encoding="UTF-8") as file_name:
        input_array = file_name.readlines()

    for line in input_array:
        line = list(map(int, line.split()))
        # print(line)
        n = next_in_list(line)
        # print(line)
        total += n

    print(total)


def next_in_list(the_list: list) -> int:

    if all(x == 0 for x in the_list):
        return 0
    else:
        list_of_dif = [j-i for i, j in zip(the_list[:-1], the_list[1:])]
        next_element_dif = next_in_list(list_of_dif)
        the_list.append(the_list[-1]+next_element_dif)
        return the_list[-1]


if __name__ == "__main__":
    main()
