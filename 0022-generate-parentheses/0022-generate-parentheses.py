class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        
        def backTrack(path, leftAddedSoFar, rightAddedSoFar):
            if len(path) == 2 * n:
                res.append("".join(path))  # 把列表转换成字符串并加入结果集
                return
            
            if leftAddedSoFar < n:
                path.append('(')  # 选择加入左括号
                backTrack(path, leftAddedSoFar + 1, rightAddedSoFar)
                path.pop()  # 回溯（撤销选择）

            if rightAddedSoFar < leftAddedSoFar:
                path.append(')')  # 选择加入右括号
                backTrack(path, leftAddedSoFar, rightAddedSoFar + 1)
                path.pop()  # 回溯（撤销选择）
        
        backTrack([], 0, 0)
        return res
