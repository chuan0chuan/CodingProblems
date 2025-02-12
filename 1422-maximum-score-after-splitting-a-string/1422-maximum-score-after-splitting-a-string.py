class Solution:
    def maxScore(self, s: str) -> int:
        totalOnes = s.count('1')
        zero_count = 0
        one_count = 0
        ans = float('-inf')
        for i in range(len(s)):
            if int (s[i]) == 0:
                zero_count += 1
            else :
                one_count +=1
            cur = zero_count + totalOnes - one_count
            ans = max(cur, ans)
        return ans
            

