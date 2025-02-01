class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backTack(0,nums, result, path)
        return result
    
    def backTack(self, startIndex,nums, result, path):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backTack(i + 1,nums, result, path)
            path.pop()
