class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = defaultdict(int)
        for c in s:
            freqMap[c] += 1
        max_freq = max(freqMap.values())
        if max_freq > (len(s) + 1) // 2:
            return ""  # 直接返回，无法重组
        result = ""
        max_heap = []
        for key, val in freqMap.items():
            heapq.heappush(max_heap, (-val,key))
        
        while len(max_heap)> 1:
            temp = []
            freq, char = heapq.heappop(max_heap)
            result += char
            freq = -freq
            freq -= 1
            freq2, char2 = heapq.heappop(max_heap)
            result += char2
            freq2 = -freq2
            freq2 -= 1

            if freq > 0:
                temp.append((-freq,char))
            if  freq2>0 :
                temp.append((-freq2,char2))
            for item in temp:
                heapq.heappush(max_heap, item)


        if max_heap:
            result += heapq.heappop(max_heap)[1]

        return result