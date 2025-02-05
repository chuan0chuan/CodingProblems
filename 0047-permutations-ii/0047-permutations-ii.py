class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backTrack(nums, result, [], [False]* len(nums))
        return result
    
    def backTrack(self, nums, result, path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(0, len(nums)):
            if (i > 0 and nums[i] == nums[i-1] and not used[i-1]) or used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backTrack(nums, result, path,used )
            path.pop()
            used[i] = False
