graph = []

for line in open("/Users/workMac/Desktop/edges.txt"):
    line = line.strip()
    line = line.split(' ')

    newLine = []
    for i in range(3):
        newLine.append(int(line[i]))
    graph.append(newLine)

print(graph)
########################################################
graphV = set()
for edge in graph:
    graphV.add(edge[0])
    graphV.add(edge[1])
#######################################################
X = set()
X.add(graph[0][0])
T = []

while X != graphV:

    minCrossing = 1000000;
    newVertex = 0

    for vertex in X:
        for edge in graph:
            if (edge[0] == vertex) and (not edge[1] in X):
                if edge[2] < minCrossing:
                    minCrossing = edge[2]
                    newVertex = edge[1]
            if (edge[1] == vertex) and (not edge[0] in X):
                if edge[2] < minCrossing:
                    minCrossing = edge[2]
                    newVertex = edge[0]

    X.add(newVertex)
    T.append(minCrossing)
######################################################
result = 0
for value in T:
    result += value
print(result)