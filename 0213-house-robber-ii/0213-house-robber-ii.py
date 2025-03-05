class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        def rob_linear(house):
            dp = [0] *len(house)
            dp[0] = house[0]
            if len(house) == 1:
                return house[0]
            dp[1] = max(house[0], house[1])
            for i in range(2,len(house)):
                dp[i] = max(dp[i-2] + house[i], dp[i-1])
            return dp[-1]
        
        result1 = rob_linear(nums[1:])
        result2 = rob_linear(nums[:-1])
        if result1>result2:
            return result1
        else:
            return result2