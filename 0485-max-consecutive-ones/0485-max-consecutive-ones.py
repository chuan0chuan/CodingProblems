class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        for d in nums:
            if d == 1:
                ans += 1
                res = max(ans,res)
            else:
                ans = 0
        return res