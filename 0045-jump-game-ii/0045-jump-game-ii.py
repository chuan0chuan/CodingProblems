class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        fast = 0
        for i in range(len(nums) -1):
            fast = max(fast, nums[i] + i)
            if i == end:
                jumps += 1
                end =fast

        return jumps