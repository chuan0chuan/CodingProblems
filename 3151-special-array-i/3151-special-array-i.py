class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 0 :
            return False

        if len(nums) == 1 :
            return True
        
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) %2 == 0:
                return False
        return True