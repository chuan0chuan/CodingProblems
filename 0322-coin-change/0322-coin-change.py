class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = [amount + 1] *(amount + 1)
        min_coin[0] = 0
        for current in range(1, amount + 1):
            for coin in coins:
                if current - coin >= 0 :
                    min_coin[current] = min(min_coin[current],  1 + min_coin[current-coin])
        if min_coin[-1] != (amount + 1):
            return min_coin[-1]
        else:
            return -1

            