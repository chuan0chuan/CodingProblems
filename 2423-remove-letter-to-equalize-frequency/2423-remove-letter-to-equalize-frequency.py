class Solution:
    def equalFrequency(self, word: str) -> bool:
        #{'a':1, 'b':1, 'c':2}
        counter = Counter(word)
        for c in word:
            counter[c] -=1
            if counter[c] == 0:
                del counter[c]

            if len(set(counter.values()))==1:
                return True
            
            counter[c] +=1
            
        return False
        