class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b) ,val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        def bfs(src, dst):
            if src not in graph or dst not in graph :
                return -1.0
            if src == dst:
                return 1.0
            
            q = deque([(src, 1.0)])
            visited = set([src])
            while q:
                node, cur_val = q.popleft()
                if node == dst:
                    return cur_val
                for nei, val in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei,cur_val * val))
            return -1.0
        
        res =[]
        for x, y in queries:
            res.append(bfs(x,y))
        return res










