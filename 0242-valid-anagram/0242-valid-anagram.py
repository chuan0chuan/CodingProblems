class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        for ch in t:
            count[ch] -= 1
            if count[ch] < 0:
                return False
        
        return True