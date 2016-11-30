# ############## List 2 String ###############
def list2String(alist):
    newString = ''
    for char in alist:
        newString += str(char)
    return newString

# ############## Read file contents ##############
vertexs = []
for line in open("/Users/hanying/Desktop/clustering_big.txt"):
    line = line.strip()
    line = line.split(' ')

    newline = list2String(line)

    if len(vertexs) < 20000:
        vertexs.append(newline)

print(len(vertexs))

# ############## Delete same vertex ##############
vertexs = list(set(vertexs))
vertexCounts = len(vertexs)
print(vertexCounts)

# ############## XOR two Strings ##############
def stringXOR(string1, string2):
    if len(string1) != len(string2):
        return

    result = ''
    for i in range(len(string1)):
        bitXOR = int(string1[i]) ^ int(string2[i])
        result += str(bitXOR)

    return result

# ############## Produce diff Strings ##############
diffVertexs = []
diffVertexStrings = []

for i in range(24):
    v = []
    for j in range(24):
        if i == j:
            v.append(1)
        else:
            v.append(0)
    diffVertexs.append(v)

firstVertexs = diffVertexs[:]
for line in firstVertexs:
    firstIndex = line.index(1)
    for i in range(firstIndex+1, 24):
        newline = line[:]
        newline[i] = 1
        diffVertexs.append(newline)

for diffVertex in diffVertexs:
    diffVertexString = list2String(diffVertex)
    diffVertexStrings.append(diffVertexString)
    #print(diffVertexString)

# ############## Union operation #############
def find(indicates, index):
    return indicates[index]

def union(indicates, index1, index2):
    print('xxxxxx')
    indicate1 = find(indicates,index1)
    indicate2 = find(indicates,index2)

    if indicate1 != indicate2:
        if indicate1 < indicate2:
            biggerIndicate = indicate2
            smallerIndicate = indicate1
        else:
            biggerIndicate = indicate1
            smallerIndicate = indicate2

        for i in range(len(indicates)):
            if indicates[i] == biggerIndicate:
                indicates[i] = smallerIndicate

########################
clusterIndicates = []
for i in range(vertexCounts):
    clusterIndicates.append(i)

for i in range(len(vertexs)):
    print(i)
    vertexString = vertexs[i]
    if clusterIndicates[i] != 1:
        for diffString in diffVertexStrings:
            diffResult = stringXOR(vertexString, diffString)

            li = vertexs[i+1:]
            if diffResult in li:
                pp = li.index(diffResult)
                union(clusterIndicates, i, pp)

print(len(set(clusterIndicates)))