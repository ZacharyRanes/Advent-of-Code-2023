input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

route = input_array[0].strip()
input_array = input_array[2:]
path = {}
for n in input_array:
    path[n.split()[0]] = (n.split()[2][1:-1], n.split()[3][:-1])

nodes = []

for k in path:
    if k[2] == "A":
        nodes.append(k)

route_index = 0
l = []

for current_node in nodes:
    steps = 0
    while current_node[2] != "Z":
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
    l.append(steps)

print("Find the lcd of these numbers", l)

##### <copy pasta>

def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)

for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])

print(lcm)

#### </copy pasta>