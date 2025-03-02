class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        
        def backTrack( s, l, r):
            if len(s) == 2 * n :
                return res.append(s)
            
            if l< n :
                backTrack(s + '(', l + 1, r)
            if r < l:
                backTrack(s + ')', l , r + 1)
        
        backTrack('', 0,0)
        return res