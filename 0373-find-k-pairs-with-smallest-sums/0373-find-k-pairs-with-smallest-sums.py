class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2:
            return res
        
        # 初始化最小堆
        # 每个堆元素是一个三元组：(和, nums1 的索引, nums2 的索引)
        # 初始时，每个 nums1[i] 与 nums2[0] 配对
        min_heap = []
        for i in range(len(nums1)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # 每次从堆中取出当前最小的配对，并将该配对所在行的下一个元素入堆
        while k > 0 and min_heap:
            cur_sum, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                # 将同一行的下一个配对放入堆
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
            k -= 1
        return res
        