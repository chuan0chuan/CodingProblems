class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = defaultdict(int)
        for c in s:
            freqMap[c] += 1

        max_heap = []
        for key , value in freqMap.items():
            heapq.heappush(max_heap, (-value, key))


        result = ""
        # 当堆不为空时，每次弹出一个元素，(-freq, char) 中 freq 为负数
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            # -freq 就是字符出现的次数
            result += char * (-freq)
        
        return result
