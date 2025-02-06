class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = nums[i] * nums[j]
                ans += freq[key]
                freq[key] +=1
        return 8*ans