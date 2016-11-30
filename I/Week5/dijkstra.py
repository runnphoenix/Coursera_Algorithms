# read graph
graph = list()
for fileLine in open("/Users/hanying/Desktop/dijkstraData.txt"):
    fileLine = fileLine.strip()
    lineElements = list()
    for element in fileLine.split():
        lineElements.append(element)
    graph.append(lineElements)

# init S U dis()
S = list()
U = list()
dis = list()

S.append(1)

for index in range(2, 201):
    U.append(index)

for index in range(0, 200):
    dis.append(1000000)

dis[0] = 0
firstLine = graph[0]
for tuple in firstLine[1:]:
    elements = tuple.split(',')
    vertex = int(elements[0])
    distance = int(elements[1])
    dis[vertex - 1] = distance

# Loop
while len(U) > 0:

    smallestDistance = 1000000
    
    for v in U:
        if dis[v-1] < smallestDistance:
            smallestDistance = dis[v-1]
            nextPoint = v

    line = graph[nextPoint-1]

    for tuple in line[1:]:
        elements = tuple.split(',')
        vertex = int(elements[0])
        distance = int(elements[1])
        
        if dis[nextPoint - 1] + distance < dis[vertex - 1]:
            dis[vertex - 1] = dis[nextPoint - 1] + distance
        # 删除遍历过的边
        line.remove(tuple)
        anotherLine = graph[vertex - 1]
        for ele in anotherLine:
            if ele == str(nextPoint) + ',' + str(distance):
                anotherLine.remove(ele)

    S.append(nextPoint)
    U.remove(nextPoint)

# print result
requiredIndex = [7,37,59,82,99,115,133,165,188,197]
for pp in requiredIndex:
    print(dis[pp-1])
