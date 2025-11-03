class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        nums = 0
        for ch in s:
            if ch.isdigit():
                nums = nums * 10 + int(ch)
            elif ch == '[':
                stack.append((cur_str, nums))
                cur_str, nums = "" , 0
            elif ch == ']':
                prev, numtorepeat = stack.pop()
                cur_str = prev + numtorepeat * cur_str
            else:
                cur_str += ch
        
        return cur_str