class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        used = [False] * len(tiles)
        tiles = sorted(tiles)
        return self.backtracking(tiles, used)
    def backtracking(self, tiles, used):
        count = 0
        for i in range(len(tiles)):
            if used[i] or ( i > 0 and tiles[i] == tiles [i-1] and not used[i-1]):
                continue
            used[i] =True
            count += 1 + self.backtracking(tiles,used )
            used[i] = False
        return count