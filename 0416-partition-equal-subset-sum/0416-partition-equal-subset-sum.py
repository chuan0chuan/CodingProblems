class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0
        dp = [0] * 10001
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        
        target = _sum // 2
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        
        if dp[target] == target:
            return True
        return False