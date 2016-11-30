####### 1.Get Graph from File #######
graph = []
for i in range(875715):
        graphLine = []
        graphLine.append(i)
        graph.append(graphLine)
#print(graph)

for fileLine in open("/Users/hanying/Desktop/SCC.txt"):
	fileLine = fileLine.strip()
	fileLine = fileLine.split(' ')
	
        firstVertex = int(fileLine[0])
        secondVertex = int(fileLine[1])

        graph[firstVertex].append(secondVertex)

#for graphLine in graph:
#        print(graphLine)

####### 2.Get Reversed Graph #######
reversedGraph = []
for i in range(875715):
        graphLine = []
        graphLine.append(i)
        reversedGraph.append(graphLine)

for graphLine in graph:
        if len(graphLine) > 1:
                for vertex in graphLine[1:]:
                        reversedGraph[vertex].append(graphLine[0])

for graphLine in reversedGraph:
        print(graphLine)

####### 2.5 Delete empty lines #######
for graphLine in graph:
        if len(graphLine) == 1:
                graph.pop(graph.index(graphLine))
print(graph)


####### 3.First Topological Sorting #######


####### 4.Second Topological Sorting #######
