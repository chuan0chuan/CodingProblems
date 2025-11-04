class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        
        teams = list(votes[0])
        teams.sort(key=lambda x: count[x])
        return ''.join(teams)