class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap =[]
        for num in arr:
            if k > 0:
                heapq.heappush(min_heap,num)
                k -= 1
            elif abs(min_heap[0] - x) > abs(num - x):
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,num)

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))
        return result
