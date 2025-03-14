class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):

            dp[i] = dp[i - 1] + dp[i - 2]
            print(f"After iteration {i}: dp = {dp}")  # 打印当前 dp 数组

        return dp[n]
