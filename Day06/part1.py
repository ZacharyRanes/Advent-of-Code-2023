input_array = []

with open('input', 'r', encoding="UTF-8") as file_name:
    input_array = file_name.readlines()

times = list(map(int, input_array[0].split()[1:]))
distances = list(map(int, input_array[1].split()[1:]))
data = zip(times, distances)

wins = []
for d in data:
    w = 0
    for i in range(d[0]+1):
        travel = i * (d[0] - i)
        print(travel)
        if travel > d[1]:
            w += 1
    # print("wins", w)
    wins.append(w)

print(wins)

t = 0
for w in wins:
    if t == 0:
        t = w
    else:
        t = t * w
print(t)
