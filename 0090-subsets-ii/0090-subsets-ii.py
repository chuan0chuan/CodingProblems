class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己
        # if startIndex >= len(nums):  # 终止条件可以不加
        #     return
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()