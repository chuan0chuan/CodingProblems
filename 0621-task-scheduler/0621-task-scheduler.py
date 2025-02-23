class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_heap =[]
        for count in freq:
            if count > 0:
                heapq.heappush(max_heap, -count)
        
        time = 0

        while max_heap:
            cycle = n +1
            temp =[]
            while cycle > 0 and max_heap:
                count = - heapq.heappop(max_heap)
                time += 1
                cycle -=1
                if count - 1 > 0:
                    temp.append(-(count - 1))
            for item in temp:
                heapq.heappush(max_heap, item)
            
            if max_heap:
                time += cycle
        return time