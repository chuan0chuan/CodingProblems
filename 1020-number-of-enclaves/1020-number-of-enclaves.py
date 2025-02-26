class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0
            dfs(r +1, c)
            dfs(r -1, c)
            dfs(r, c +1)
            dfs(r, c -1)
        
        for r in range(rows):
            for c in [0, cols - 1]:
                if grid[r][c] ==1 :
                    dfs(r, c)

        for c in range(cols):
            for r in [0, rows - 1]:
                if grid[r][c] ==1:
                    dfs(r,c)
        return sum(row.count(1) for row in grid)

