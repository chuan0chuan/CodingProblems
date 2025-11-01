class Leaderboard:

    def __init__(self):
        self.score_map = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.score_map:
            self.score_map[playerId] = 0
        self.score_map[playerId] += score

    def top(self, K: int) -> int:
        scores = sorted(self.score_map.values(), reverse = True)
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.score_map:
            del self.score_map[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)