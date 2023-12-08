input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

route = input_array[0].strip()
input_array = input_array[2:]
path = {}
for n in input_array:
    path[n.split()[0]] = (n.split()[2][1:-1], n.split()[3][:-1])

current_node = "AAA"
route_index = 0
steps = 0
while current_node != "ZZZ":
    if route[route_index] == 'R':
        # print(current_node, "next", path[current_node][1], "R")
        current_node = path[current_node][1]
    else:
        # print(current_node, "next", path[current_node][0], "L")
        current_node = path[current_node][0]
    steps += 1

    route_index += 1
    if route_index >= len(route):
        route_index = 0

print(steps)
