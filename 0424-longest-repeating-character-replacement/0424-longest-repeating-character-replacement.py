class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        l = 0
        max_count = 0
        ans = 0

        for r, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            cnt[idx] += 1
            max_count = max(max_count, cnt[idx])

            while (r-l+1) - max_count > k:
                cnt[ord(s[l]) - ord('A')] -= 1
                l+=1
            
            ans = max(ans, r - l +1)
        return ans