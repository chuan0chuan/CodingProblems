class Solution:
    def trackBack(self, candidates: List[int], target: int, curSum:int, startIndex:int, path, result):
        if curSum > target:
            return
        if curSum == target:
            result.append(path[:])
        for i in range(startIndex,len(candidates)):
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            curSum += candidates[i]
            self.trackBack(candidates,target,curSum,i + 1, path,result)
            curSum -= candidates[i]
            path.pop()
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        candidates.sort()
        self.trackBack(candidates, target, 0, 0, [],result)
        return result