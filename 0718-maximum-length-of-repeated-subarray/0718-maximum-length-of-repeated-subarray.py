class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans =0 
        #nums1 represent row and nums2 represent column
        dp = [[0] * (len(nums2) + 1)for _ in range(len(nums1) + 1)]
        # dp[i] mean index with i-1 in nums list
        for i in range(1,len(nums1) + 1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans
