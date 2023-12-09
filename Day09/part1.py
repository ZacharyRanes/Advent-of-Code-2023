total = 0
input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

for line in input_array:
    line = list(map(int, line.split()))
    history = []
    history.append(line)
    # check if every item in the list is the same
    while any(x != history[-1][0] for x in history[-1]):
        # add a new list to history that is the differences of the last list
        history.append([j-i for i, j in zip(history[-1][:-1], history[-1][1:])])

    # for h in history:
    #     print(h)

    history.reverse()
    dif = 0
    for h in history:
        dif += h[-1]
        # print(h, dif)
    total += dif

print(total)
