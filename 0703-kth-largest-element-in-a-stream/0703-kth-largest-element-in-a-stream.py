class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.kth:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.kth:
            heapq.heappush(self.min_heap, val)
        else:
            if val > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, val)
        
        return self.min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)