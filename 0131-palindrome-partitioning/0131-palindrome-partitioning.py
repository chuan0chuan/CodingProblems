class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backTracking([], result, s, 0)
        return result

    def backTracking(self, path, result, s: str, startIndex):
        if startIndex == len(s):
            result.append(path[:])
            return
        
        for i in range(startIndex, len(s)):
            if s[startIndex: i + 1] == s[startIndex: i + 1][::-1]:
                path.append(s[startIndex: i + 1])
                self.backTracking(path, result,s, i +1 )
                path.pop()