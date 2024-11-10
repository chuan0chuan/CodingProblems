class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index = len(s) - 1 #cookie
        result = 0
        for i in range(len(g)- 1, -1 , -1):
            if index >= 0 and s[index] >= g[i]:
                index -= 1
                result += 1
        return result 