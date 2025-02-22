class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
    
        for i in range(len(matrix)):
            heapq.heappush(heap,(matrix[i][0], i , 0))

        while k :
            val, rowIdx, colIdx = heapq.heappop(heap)
            k = k - 1
            if k == 0:
                return val
            if colIdx < len(matrix) -1 :
                heapq.heappush(heap, (matrix[rowIdx][colIdx + 1], rowIdx , colIdx + 1))
            
