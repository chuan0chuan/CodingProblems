class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        rank = defaultdict(int)
        for index, number in enumerate(sortedNums):
            rank.setdefault(number, index)
        
        return [ rank[num] for num in nums]