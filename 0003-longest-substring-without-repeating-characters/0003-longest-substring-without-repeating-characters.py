class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        result = 0
        for right ,c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] +1
            seen[c] = right
            result = max(result, right - start + 1)
        return result