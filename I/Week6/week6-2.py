from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return int(- self.small[0])
        else:
            return int(self.large[0])


result = 0
finder = MedianFinder()

for line in open("/users/hanying/Desktop/Median.txt"):
    line = line.strip()
    finder.addNum(int(line))
    result += finder.findMedian()

print(result)
print(result % 10000)
