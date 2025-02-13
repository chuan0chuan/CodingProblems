class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
        count = 0
        for i in range(len(words)):
            for j in range (i + 1, len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    count += 1
        return count
