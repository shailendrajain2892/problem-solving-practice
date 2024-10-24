import heapq


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], [] # maxHeap(because we want max num of small number on top),
        # minHeap(because we want small number from the large num on top)

    def addNum(self, num: int) -> None:
        # decide where to put the num
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        # balance the heap by checking the size
        if len(self.small) > len(self.large) + 1:
            num = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0]+self.large[0])/2
    
mf = MedianFinder()
mf.addNum(5)
mf.addNum(3)
print(mf.findMedian())
