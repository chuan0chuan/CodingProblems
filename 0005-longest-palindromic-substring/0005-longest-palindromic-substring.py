class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_ans = ""
        largeThree = 0
        for i in range(n):
            dp[i][i] = True
            max_ans = s [i: i+1]

        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_ans = s [i: i+2]
        
        for length in range(3, n + 1):
            for i in range(n - length +1):
                if s[i] == s[i + length - 1] and dp[i+ 1][i + length - 2] == True:
                    dp[i][i + length - 1] = True
                    max_ans = s[i : i + length]

        return max_ans


        