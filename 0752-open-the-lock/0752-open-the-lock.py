class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        
        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            status, step = q.popleft()
            if status == target:
                return step
            for nextone in self.nextStates(status):
                if nextone not in dead and nextone not in visited:
                    visited.add(nextone)
                    q.append((nextone, step+1))
        return -1
        

    def nextStates(self, status):
        res = []
        for i in range(4):
            digit = int(status[i])
            for move in (-1,1):
                new_digit = (digit + move) % 10
                new_state = status[:i] + str(new_digit) + status[i+1:]
                res.append(new_state)
        return res