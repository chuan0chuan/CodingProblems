class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        rows, col = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= col or grid[r][c] != '1':
                return 
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
    
        return count
