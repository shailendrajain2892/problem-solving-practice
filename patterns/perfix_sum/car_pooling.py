import heapq
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key=lambda x: x[1])
        minHeap=[] # [end,numPass]
        currPass=0
        for t in trips:
            numPass, start, end = t
            while minHeap and start >= minHeap[0][0]:
                currPass-=minHeap[0][1]
                heapq.heappop(minHeap)
            currPass+=numPass
            if currPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
            
        return True