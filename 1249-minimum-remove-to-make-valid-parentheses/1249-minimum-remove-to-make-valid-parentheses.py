class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
                result.append(ch)
            elif ch== ')':
                if balance > 0:
                    balance -=1
                    result.append(ch)
            else:
                result.append(ch)
        
        final = []
        balance = 0
        for ch in reversed(result):
            if ch == ')':
                balance += 1
                final.append(ch)
            elif ch =='(':
                if balance > 0:
                    balance -= 1
                    final.append(ch)
            else:
                final.append(ch)
        
        return "".join(reversed(final))