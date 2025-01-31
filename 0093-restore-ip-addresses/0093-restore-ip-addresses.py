class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
       
        result = []
        self.backtracking(s, 0, [], result)
        return result
    
    def backtracking(self, s, startIndex, path, result):
        if startIndex == len(s):
            result.append('.'.join(path[:]))
            return
        
        for i in range(startIndex, startIndex+3):
            # 如果 i 往后遍历了，并且当前地址的第一个元素是 0 ，就直接退出
            if i > startIndex and s[startIndex] == '0':
                break
            # 比如 s 长度为 5，当前遍历到 i = 3 这个元素
            # 因为还没有执行任何操作，所以此时剩下的元素数量就是 5 - 3 = 2 ，即包括当前的 i 本身
            # path 里面是当前包含的子串，所以有几个元素就表示储存了几个地址
            # 所以 (4 - len(path)) * 3 表示当前路径至多能存放的元素个数
            # 4 - len(path) 表示至少要存放的元素个数
            if (4 - len(path)) * 3 < len(s) - i or 4 - len(path) > len(s) - i:
                break
            if i - startIndex == 2:
                if not int(s[startIndex:i+1]) <= 255:
                    break
            path.append(s[startIndex:i+1])
            self.backtracking(s, i+1, path, result)
            path.pop()