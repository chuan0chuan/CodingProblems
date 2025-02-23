class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqMap = defaultdict(int)
        max_heap =[]
        for word in words:
            freqMap[word] += 1
        
        for key, value in freqMap.items():
            heapq.heappush(max_heap, (-value,key))
        result =[]
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        return result
        
