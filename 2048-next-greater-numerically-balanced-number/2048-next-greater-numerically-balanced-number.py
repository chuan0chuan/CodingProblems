from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        res = set()

        # 对 multiset 做去重全排列，生成所有排列对应的整数
        def permute_from_counts(cnt: Counter, length: int):
            path = []
            def dfs():
                if len(path) == length:
                    res.add(int("".join(path)))
                    return
                # 为了稳定性，也为了更快遇到较小数，这里按字符升序尝试
                for ch in list(cnt.keys()):
                    if cnt[ch] > 0:
                        cnt[ch] -= 1
                        path.append(ch)
                        dfs()
                        path.pop()
                        cnt[ch] += 1
            dfs()

        # 按 d=1..6 决定“是否选这个数字 d（出现 d 次）”
        def build_bags(d: int, bag: list[str]):
            if d == 7:
                if 1 <= len(bag) <= 7:   # 只生成题目范围内的排列
                    permute_from_counts(Counter(bag), len(bag))
                return
            # 1) 不选 d
            build_bags(d + 1, bag)
            # 2) 选 d（追加 d 个字符 d）
            bag.extend([str(d)] * d)
            # 剪枝：长度超过 7 就没必要继续（不会是答案）
            if len(bag) <= 7:
                build_bags(d + 1, bag)
            # 回溯
            del bag[-d:]

        build_bags(1, [])

        candidates = sorted(x for x in res if x > n)
        return candidates[0] if candidates else -1
