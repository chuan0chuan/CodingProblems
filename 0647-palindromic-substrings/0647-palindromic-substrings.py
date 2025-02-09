class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        ans = 0
        # for i in range(n):
        #     dp[i][i] = True
        #     ans += 1

        # for i in range(n - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i+1]=True
        #         ans += 1
        
        # for length in range(3, n + 1):
        #     for i in range(n - length + 1):
        #         if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
        #             palindrome[i][i + length - 1] = True
        #             ans += 1

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length<= 2 or dp[i+1][j-1]):
                    dp[i][j] =True
                    ans += 1
        return ans
            