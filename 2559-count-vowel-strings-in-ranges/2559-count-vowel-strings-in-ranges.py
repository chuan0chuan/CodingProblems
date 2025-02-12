class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]: 
        def checkVowel(word):
            return word[0] in {'a', 'e', 'i', 'o', 'u'} and word[-1] in {'a', 'e', 'i', 'o', 'u'}
                
        # 计算前缀和数组
        n = len(words)
        prefix_sum = [0] * (n + 1)  # prefix_sum[i] 表示前 i 个单词中满足条件的个数
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if checkVowel(words[i]) else 0)
        
        # 处理查询
        result = []
        for left, right in queries:
            result.append(prefix_sum[right + 1] - prefix_sum[left])
        
        return result
