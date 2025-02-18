class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        numberOne = 0  # 统计1的个数
        horizontal_pairs = 0  # 横向相连的1的数量
        vertical_pairs = 0  # 纵向相连的1的数量
        
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    numberOne += 1  # 统计1的个数
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        horizontal_pairs += 1  # 统计横向相连的数量
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        vertical_pairs += 1  # 统计纵向相连的数量

        # 计算周长
        return numberOne * 4 - (horizontal_pairs + vertical_pairs) * 2
