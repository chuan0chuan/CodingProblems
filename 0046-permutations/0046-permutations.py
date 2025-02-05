class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backTrack(nums, [], set(),result)
        return result
    
    def backTrack(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num in used:
                continue
            used.add(num)
            path.append(num)
            self.backTrack(nums, path, used, result)
            path.pop()
            used.remove(num)