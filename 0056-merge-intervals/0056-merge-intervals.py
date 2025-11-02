class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key = lambda x:x[0])

        result = []
        
        for i in range(len(intervals)):
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1],result[-1][1])
        
        return result