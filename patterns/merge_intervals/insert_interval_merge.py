class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        def insertNewInterval(intervals, newInterval):
            if not intervals:
                return [newInterval]
            oldIntervals = intervals
            for idx, interval in enumerate(intervals):
                if newInterval[0] < interval[0]:
                    intervals.insert(idx, newInterval)
                    break
            if len(oldIntervals) == len(intervals):
                intervals.append(newInterval)
            return intervals
        
        updatedIntervals = insertNewInterval(intervals, newInterval)

        def merge_intervals(updatedIntervals):
            result = []
            startTime = updatedIntervals[0][0]
            endTime = updatedIntervals[0][1]
            for i in range(1, len(updatedIntervals)):
                currentStartTime = updatedIntervals[i][0]
                currentEndTime = updatedIntervals[i][1]

                if currentStartTime <= endTime:
                    endTime = max(endTime, currentEndTime)
                else:
                    result.append([startTime, endTime])
                    startTime = currentStartTime
                    endTime = currentEndTime
            result.append([startTime, endTime])
            return result
        return merge_intervals(updatedIntervals)
    
# print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
intervals = [[1,5]]
newInterval = [2,7]
print(Solution().insert(intervals, newInterval))