class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1,n):
            new_s = []
            count = 1
            for i in range(1, len(s) + 1):
                if i == len(s) or s[i] != s[i-1]:
                    new_s.append(str(count))
                    new_s.append(s[i-1])
                    count = 1
                else:
                    count+=1
            
            s = "".join(new_s)
        return s