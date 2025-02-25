class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            dis = (point[0] * point[0]) + (point[1] * point[1])
            heapq.heappush(min_heap, (dis, point))
        
        result = []
        for _ in range(k):
            if min_heap:
                result.append(heapq.heappop(min_heap)[1])
        
        return result