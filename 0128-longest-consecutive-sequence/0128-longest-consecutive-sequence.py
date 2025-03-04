class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_list = sorted(set(nums))
        
        max_length = 1
        current_length = 1
        
        for i in range(1, len(sorted_list)):
            if sorted_list[i] - sorted_list[i-1] == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        max_length = max(max_length, current_length)
        
        return max_length