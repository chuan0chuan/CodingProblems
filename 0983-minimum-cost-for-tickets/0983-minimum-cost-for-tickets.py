class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = 366 * [0]
        travel = set(days)

        for i in range(1,366):
            if i not in travel:
                dp[i] = dp[i-1]
            else:
                cost1 = dp[i -1] +costs[0]
                cost2 = max(0,dp[i-7]) + costs[1]
                cost3 = max(0,dp[i-30]) + costs[2]
                dp[i] = min(cost1, cost2, cost3)
        return dp[365]