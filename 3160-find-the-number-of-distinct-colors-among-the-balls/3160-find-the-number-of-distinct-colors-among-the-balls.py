class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = defaultdict(int)
        color_freq = defaultdict(int)
        result = []

        for x, y in queries:
            if x in ball_color:
                old_color = ball_color[x]
                color_freq[old_color] -= 1
                if color_freq[old_color] == 0:
                    del color_freq[old_color]
            ball_color[x] = y
            color_freq[y] += 1
            result.append(len(color_freq))
        
        return result

