class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = cur_sum
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]

            ans = max(cur_sum, max_sum)
            
        return ans