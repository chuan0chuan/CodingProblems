class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
            result = []
            path = [0]
            def dfs(node: int):
                if node == (len(graph) - 1):
                    result.append(path[:])
                    return
                for i in graph[node]:
                    path.append(i)
                    dfs(i)
                    path.pop()

            dfs(0)
            return result
