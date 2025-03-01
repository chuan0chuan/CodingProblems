class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        count = 0
        row = len(board)
        col = len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != 'X':
                return
            board[r][c] = '.'
            dfs(r + 1, c)
            dfs(r - 1 ,c)
            dfs(r, c +1)
            dfs(r, c -1)

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'X':
                    count += 1
                    dfs(r, c)
        return count

