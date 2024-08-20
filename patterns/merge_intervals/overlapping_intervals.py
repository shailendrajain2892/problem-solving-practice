class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        startTime = intervals[0][0]
        endTime = intervals[0][1]
        for i in range(1, len(intervals)):
            currentStartTime = intervals[i][0]
            currentEndTime = intervals[i][1]

            if currentStartTime <= endTime:
                endTime = max(endTime, currentEndTime)
            else:
                result.append([startTime, endTime])
                startTime = currentStartTime
                endTime = currentEndTime

        result.append([startTime, endTime])
        return result
    
print(Solution().merge([[1,10],[4,6],[8,10],[15,18]]))