# ####### Read datas #######
data = []
W = itemCount = 0

for line in open("/users/workMac/Desktop/knapsack1.txt"):
    line = line.strip()
    line = line.split(' ')
    newline = []
    for number in line:
        newline.append(int(number))
    data.append(newline)

W = data[0][0]
itemCount = data[0][1]
data.pop(0)

# ####### Initial Aray #######
results = [[0 for col in range(W)] for row in range(itemCount)]
for i in range(1, itemCount):
    for x in range(W):
        w = data[i][1]
        v = data[i][0]
        if x < w:
            results[i][x] = results[i-1][x]
        else:
            results[i][x] = max(results[i-1][x], results[i-1][x-w] + v)

# #######  #######
print(results[itemCount-1][W-1])