digits = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

for line in input_array:

    for i, c in enumerate(line):
        if c.isdigit():
            d1 = c
            break
    for d in digits:
        di = line.find(d)
        if di != -1 and di < i:
            i = di
            d1 = digits[d]

    for i, c in reversed(list(enumerate(line))):
        if c.isdigit():
            d2 = c
            break
    for d in digits:
        di = line.rfind(d)
        if di != -1 and di > i:
            i = di
            d2 = digits[d]

    # print(d1, d2)

    total +=(int(d1+d2))
print(total)