input_array = []

with open('input_test2', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

route = input_array[0].strip()
input_array = input_array[2:]
path = {}
for n in input_array:
    path[n.split()[0]] = (n.split()[2][1:-1], n.split()[3][:-1])

current_nodes = []

for k in path:
    if k[2] == "A":
        current_nodes.append(k)

route_index = 0
steps = 0
while any(node[2] != "Z" for node in current_nodes):
    # print(current_nodes)
    if route[route_index] == 'R':
        for j in range(len(current_nodes)):
            current_nodes[j] = path[current_nodes[j]][1]
    else:
        for j in range(len(current_nodes)):
            current_nodes[j] = path[current_nodes[j]][0]
    steps += 1

    route_index += 1
    if route_index >= len(route):
        route_index = 0

print(steps)
