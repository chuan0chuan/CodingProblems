class Solution:
    def trackBack(self, candidates, target,result,curSum,path,start):
        if curSum > target:
            return
        if curSum == target:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            curSum += candidates[i]
            self.trackBack(candidates, target,result,curSum,path,i)
            curSum -= candidates[i]
            path.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        curSum = 0
        self.trackBack(candidates, target,result,curSum,[], 0 )
        return result