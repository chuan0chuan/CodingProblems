class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0  # 如果越界或者是水，返回 0

            grid[r][c] = 0  # 标记访问过的陆地
            area = 1  # 当前位置的面积是 1

            # 分别递归四个方向，并累加面积
            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            right = dfs(r, c + 1)
            left = dfs(r, c - 1)

            area += down + up + right + left  # 总面积 = 当前位置 + 四个方向扩展的面积
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # 发现岛屿
                    current_area = dfs(r, c)  # 计算当前岛屿面积
                    max_area = max(max_area, current_area)  # 更新最大面积

        return max_area
