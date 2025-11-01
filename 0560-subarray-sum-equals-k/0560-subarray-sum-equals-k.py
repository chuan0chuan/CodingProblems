class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = defaultdict(int)
        sub_num[0] = 1
        total = count =0
        for n in nums:
            total += n
            
            if total - k in sub_num:
                count += sub_num[total-k]
            
            sub_num[total] +=1
        
        return count