from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap=[-v for k, v in task_count.items()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()
        while max_heap or q:
            time+=1

            if max_heap:
                cnt = 1+heapq.heappop(max_heap)     
                if cnt:      
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

print(Solution().leastInterval(['A','A','A','B','B','C', 'C'], 2))