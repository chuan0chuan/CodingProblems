class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(remaining):
            if remaining == "":
                return [""]
            if remaining in memo:
                return memo[remaining]
            
            res =[]
            for w in word_set:
                if remaining.startswith(w):
                    sub_sentences = dfs(remaining[len(w):])
                    for sub in sub_sentences:
                        if sub:
                            res.append(w + " " + sub)
                        else:
                            res.append(w)
            
            memo[remaining] = res
            return res
        
        return dfs(s)
                        