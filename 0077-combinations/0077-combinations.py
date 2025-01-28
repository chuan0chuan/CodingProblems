class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.travesalBack(n, k, 1, [], result)
        return result
    def travesalBack(self, n: int, k:int, index:int, path:List[int], result):
        # end condition:
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(index, n + 1):
            path.append(i)
            self.travesalBack(n, k, i + 1, path, result)
            path.pop()

        

