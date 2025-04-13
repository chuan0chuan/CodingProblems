class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')

        for row in range(len(nums)):
            val = nums[row][0]
            heapq.heappush(min_heap, (val, row, 0))
            max_val = max(max_val, val)
        
        best_range = [float('-inf'), float('inf')]

        while True:
            min_val, row, idx = heapq.heappop(min_heap)

            if max_val - min_val < best_range[1] - best_range[0] or (max_val - min_val == best_range[1] - best_range[0] and min_val < best_range[0]):
                best_range = [min_val, max_val]

            if idx + 1 ==len(nums[row]):
                break
            
            next_val = nums[row][idx + 1]
            heapq.heappush(min_heap, (next_val, row, idx + 1))
            max_val = max(max_val, next_val)

        return best_range