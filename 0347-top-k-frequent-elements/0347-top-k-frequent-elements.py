import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        p_que = []

        for key , freq in map_.items():
            heapq.heappush(p_que,(freq, key))
            if len(p_que) > k:
                heapq.heappop(p_que)
        
        result = [0] * k
        for i in range(k-1, -1 , -1):
            result[i] = heapq.heappop(p_que)[1]
        return result
