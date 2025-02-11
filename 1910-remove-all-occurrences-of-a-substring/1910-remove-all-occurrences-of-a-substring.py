class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        result = []
        for c in s:
            result.append(c)
            if len(result) >= n and self.find_part_inend(result, part, n):
                for i in range(n):
                    result.pop()
        return "".join(result)

    def find_part_inend(self,result, part, length):
        last =result[-length:]
        return "".join(result[-length:]) == part


