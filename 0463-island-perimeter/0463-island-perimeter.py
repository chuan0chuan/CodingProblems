class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # 每个陆地格子默认贡献4条边
                    perimeter += 4
                    
                    # 检查左边是否有相邻的陆地（水平方向）
                    if j > 0 and grid[i][j-1] == 1:
                        # 如果左边是陆地，减去两条边（当前格子和左边格子各减一条）
                        perimeter -= 2
                    
                    # 检查上边是否有相邻的陆地（垂直方向）
                    if i > 0 and grid[i-1][j] == 1:
                        # 如果上边是陆地，减去两条边（当前格子和上边格子各减一条）
                        perimeter -= 2
        
        return perimeter
