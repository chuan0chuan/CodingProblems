class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        res=0
        def l(a,b):
            len=(((a[0]-b[0])**2)+((a[1]-b[1])**2))
            return len
        d=[l(p1,p2),l(p1,p3),l(p1,p4),l(p2,p3),l(p2,p4),l(p3,p4)]
        d.sort()
        return True if 0<d[0]==d[1]==d[2]==d[3] and d[4]==d[5] else False 