class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        swap_index = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(swap_index) == 2:
            x, y = swap_index
            if s1[x] == s2[y] and s1[y] == s2[x]:
                return True
        return False