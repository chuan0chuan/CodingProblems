from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        groups = defaultdict(list)

        # 1️⃣ 解析并分组
        for t in transactions:
            name, time, amount, city = t.split(',')
            groups[name].append((int(time), int(amount), city, t))

        res = []

        # 2️⃣ 处理每个用户
        for name, trans_list in groups.items():
            # 按时间升序排列，方便 60 分钟剪枝
            trans_list.sort(key=lambda x: x[0])
            n = len(trans_list)
            is_invalid = [False] * n  # 每笔交易一个标记位

            for i in range(n):
                time_i, amount_i, city_i, raw_i = trans_list[i]

                # 条件1：金额超限
                if amount_i > 1000:
                    is_invalid[i] = True

                # 条件2：60 分钟内不同城市
                for j in range(i + 1, n):
                    time_j, amount_j, city_j, raw_j = trans_list[j]
                    if time_j - time_i > 60:
                        break
                    if city_i != city_j:
                        is_invalid[i] = True
                        is_invalid[j] = True

            # 收集该用户所有被标记的交易
            for i in range(n):
                if is_invalid[i]:
                    res.append(trans_list[i][3])

        return res
