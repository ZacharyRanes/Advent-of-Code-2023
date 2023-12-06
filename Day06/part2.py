input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

time = int("".join(input_array[0].split()[1:]))
distance = int("".join(input_array[1].split()[1:]))

# print(time, distance)

# lb
for i in range(time + 1):
    travel = i * (time - i)
    if travel > distance:
        lb = i
        break

# rb
for i in range(time + 1, -1, -1):
    travel = i * (time - i)
    if travel > distance:
        rb = i
        break


w = rb - lb + 1
print(w)
