#######
graph = []
K = 500
kr = 4
#######
for line in open("/users/workMac/Desktop/clustering1.txt"):
    line = line.strip()
    line = line.split(' ')

    if int(line[0]) <= K and int(line[1]) <= K:
        numbersLine = []
        for number in line:
            numbersLine.append(int(number))
        graph.append(numbersLine)

#######
graph.sort(key=lambda l: l[2])

#######
k = K
clusterIndex = range(1, k+1)

#######
while k >= kr:

    vertex1 = graph[0][0]
    vertex2 = graph[0][1]

    if clusterIndex[vertex1-1] < clusterIndex[vertex2-1]:
        smallerVertex = vertex1
        biggerVertex = vertex2
    else:
        smallerVertex = vertex2
        biggerVertex = vertex1

    if clusterIndex[smallerVertex-1] != clusterIndex[biggerVertex-1]:
        tmp = clusterIndex[biggerVertex-1]
        for index in range(K):
            if clusterIndex[index] == tmp:
                clusterIndex[index] = clusterIndex[smallerVertex-1]

        k -= 1
        print(graph[0])
        print(clusterIndex)

    graph.pop(0)