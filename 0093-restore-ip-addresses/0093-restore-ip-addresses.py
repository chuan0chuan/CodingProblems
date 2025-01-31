class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backTrack(s, 0, [], result)
        return result
    def backTrack(self, s , startIndex, path, result):
        if startIndex == len(s):
            result.append('.'.join(path[:]))
            return
        for i in range(startIndex, startIndex + 3):
            if s[startIndex] == '0' and i > startIndex:
                break
            if (4 - len(path))*3 < len(s) - i or 4 - len(path) > len(s) - i:
                break
            if i - startIndex == 2:
                if not int(s[startIndex: i + 1]) <= 255:
                    break
            path.append(s[startIndex: i +1])
            self.backTrack(s, i + 1,path,result)
            path.pop()