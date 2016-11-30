########################################################
data = []

for line in open("/Users/hanying/Desktop/jobs.txt"):
    line = line.strip()
    line = line.split(' ')
    line.append(int(line[0]) - int(line[1]))
    line.append(float(line[0]) / float(line[1]))
    data.append(line)
########################################################
data.sort(key=lambda l:(int(l[2]),int(l[0])),reverse=True)
print(data)
########################################################
cj = 0
result = 0
for i in range(0,len(data)):
    cj += int(data[i][1])
    result += int(data[i][0]) * cj

print(result)
########################################################
def mycmp2(a,b):
    if a[3]<b[3]:
        return 1
    if a[3]>b[3]:
        return -1
    if a[0]>b[0]:
        return 1
    if a[0]<b[0]:
        return -1
    return 0

data.sort(cmp=mycmp2)
print(data)
########################################################
cj2 = 0
result2 = 0
for i in range(0,len(data)):
    cj2 += int(data[i][1])
    result2 += int(data[i][0]) * cj2

print(result2)