class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        curSum = 0
        self.trackBack(k, n, [], result, 1,curSum)
        return result
    def trackBack(self, k: int, n: int, path:List[int], result, starIndex: int, curSum):
        if len(path) == k and curSum == n:
            result.append(path[:])
            return
        for i in range(starIndex, n + 1 ):
            path.append(i)
            curSum += i
            self.trackBack(k, n , path, result, i +1,curSum)
            curSum -= i
            path.pop()
        
