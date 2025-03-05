class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
       # step 1. define the meaning of dp
        dp = [0] * n
        #step2. figure out how to initialize 0
        dp[0] = nums[0]

        if n == 1:
            return dp[0]
        dp[1]=max(nums[1], dp[0])

        for i in range(2, n):
            #step3. know the way of status update based on previous record
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]