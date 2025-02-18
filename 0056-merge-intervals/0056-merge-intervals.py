class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        row = len(intervals)
        
        # 1. 先按照起始位置排序
        intervals.sort(key=lambda x: x[0])
        
        result = []
        
        for i in range(row):
            # 2. 如果 result 为空 或者 当前区间不重叠，直接加入
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                # 3. 如果有重叠，合并区间，更新 result 里最后一个区间的结束时间
                result[-1][1] = max(result[-1][1], intervals[i][1])
        
        return result