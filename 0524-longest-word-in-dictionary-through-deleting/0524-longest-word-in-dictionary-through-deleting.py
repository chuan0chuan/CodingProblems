class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        s_count = Counter(s)

        def is_subsequence(word, s):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)

        ans = ""

        for word in dictionary:

            # 先用Counter剪枝
            if Counter(word) - s_count:
                continue

            if is_subsequence(word, s):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans