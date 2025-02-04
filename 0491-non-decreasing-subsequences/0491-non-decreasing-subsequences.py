class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backTrack(nums, 0, result, path)
        return result
    
    def backTrack(self, nums, index, result, path):
        if len(path) >= 2:
            result.append(path[:])

        numset = set()
        for i in range(index, len(nums)):
            if nums[i] in numset or (path and nums[i]< path[-1]):
                continue
            numset.add(nums[i])
            path.append(nums[i])
            self.backTrack(nums, i+1, result, path)
            path.pop()
        