class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # for this questions we can not use heapify cause , it will make
        # 10 < 2, so we use heap.heapq.nlargest
        pq = []
        for num in nums :
            key = (len(num),num)
            heapq.heappush(pq,key)
            while len(pq) > k:
                heapq.heappop(pq)
        result = heapq.heappop(pq)
        return result[1]