class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        point= 0
        left, right = 0, len(enemyEnergies) - 1
        if currentEnergy < enemyEnergies[0]:
            return point
        totalEnergy = currentEnergy
        for j in range(len(enemyEnergies) - 1, 0, -1): totalEnergy += enemyEnergies[j]
        return totalEnergy // enemyEnergies[0]