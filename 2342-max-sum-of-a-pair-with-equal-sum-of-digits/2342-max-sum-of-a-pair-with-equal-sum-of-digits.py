class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        sum_dict = defaultdict(list)
        def checkSum( num: int):
            sum_digit =0
            for i in str(num):
                sum_digit += int (i)
            return sum_digit

        for i in range(len(nums)):
            sumAskey = checkSum(nums[i])
            sum_dict[sumAskey].append(nums[i])

        max_sum = -1
        for key,value in sum_dict.items():
            if len(value)>1:
                value.sort(reverse =True)
                max_sum = max(max_sum, value[0] + value[1])
        return max_sum

        

