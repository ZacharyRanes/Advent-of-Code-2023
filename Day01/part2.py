digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

input_array = []

with open('input1', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

total = 0

for line in input_array:

    for i, c in enumerate(line):
        if c.isdigit():
            d1 = c
            break


    for i, c in reversed(list(enumerate(line))):
        if c.isdigit():
            d2 = c
            break



    total +=(int(d1+d2))
print(total)