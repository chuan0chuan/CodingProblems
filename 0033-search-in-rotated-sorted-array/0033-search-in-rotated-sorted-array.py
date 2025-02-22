class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if ((nums[mid] < nums[0]) and (target < nums[0])):
                num = nums[mid]
            else:
                if target < nums[0]:
                    num = -math.inf
                else:
                    num = math.inf
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid
            else:
                return mid
        
        return -1