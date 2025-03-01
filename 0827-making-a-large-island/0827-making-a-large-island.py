class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_size = {}
        def dfs(r, c, island_id):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = island_id
            area = 1
            down = dfs(r + 1, c, island_id)
            up = dfs(r - 1, c , island_id)
            right = dfs(r, c + 1, island_id)
            left = dfs(r, c - 1, island_id)
            area += down + up + right + left
            return area
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c , island_id)
                    island_size[island_id] = area
                    island_id += 1
        
        max_area = max(island_size.values(), default = 0)
        for r in range(n):
            for c in range(n):
                if  grid[r][c] == 0:
                    seen  =set()
                    linked_area = 1
                    if r > 0 and grid[r - 1][c] > 1:
                        seen.add(grid[r - 1][c])
                    if r < n -1 and grid[r + 1][c] > 1:
                        seen.add(grid[r + 1][c])
                    if c > 0 and grid[r][c -1] > 1:
                        seen.add(grid[r][c -1])
                    if c < n -1 and grid[r][c + 1] >1:
                        seen.add(grid[r][c + 1])
                    for island in seen:
                        linked_area += island_size[island]
                    max_area = max(max_area, linked_area)
        if max_area > 0:
            return max_area
        else:
            return n * n