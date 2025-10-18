class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for index ,val in enumerate(nums):
            if val in seen and index - seen[val] <= k:
                return True
            else:
                seen[val] = index
        
        return False