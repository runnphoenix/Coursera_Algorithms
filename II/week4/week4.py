def getFileNames():
    names = ["g1.txt", "g2.txt", "g3.txt"]
    fileNamePre = "/users/workMac/Desktop/"
    fileNames = []
    for name in names:
        fileNames.append(fileNamePre + name)

    return fileNames

def readAGraphData(fileName):
    graph = []
    vertexCount = edgeCount = 0

    for line in open(fileName):
        line = line.strip()
        line = line.split(" ")
        if len(line) == 2:
            vertexCount = int(line[0])
            edgeCount = int(line[1])
        else:
            newline = []
            for element in line:
                newline.append(int(element))
            graph.append(newline)

    return (vertexCount, edgeCount, graph)

def floyd():
    # ####### Initial #######
    (vertexCount, edgeCount, graph) = readAGraphData("/users/workMac/Desktop/g3.txt")
    resultArr = [[0 for v1 in range(vertexCount)] for v2 in range(vertexCount)]

    for i in range(vertexCount):
        for j in range(vertexCount):
            if i != j:
                resultArr[i][j] = 99999999

    for edge in graph:
        resultArr[edge[0] - 1][edge[1] - 1] = edge[2]

    # ####### Calculate #######
    for k in range(vertexCount):
        for i in range(vertexCount):
            for j in range(vertexCount):
                resultArr[i][j] = min(resultArr[i][j], resultArr[i][k] + resultArr[k][j])

    # ####### Print Result #######
    outPutFile = open('/users/workMac/Desktop/result.txt', 'w+')

    for line in resultArr:
        outPutFile.write(str(line) + "\n")

    minValue = 99999999
    for i in range(vertexCount):
        for j in range(vertexCount):
            if i != j:
                if resultArr[i][j] < minValue:
                    minValue = resultArr[i][j]

    outPutFile.write("\n" + str(minValue))

    outPutFile.close()

# ####### Actually Run
floyd()