class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        result = 0
        diff_count = defaultdict(int)
        for index in range(len(nums)):
            diff = index - nums[index]
            good_pair= diff_count[diff]
            result += index -good_pair
            diff_count[diff] += 1
        return result
            