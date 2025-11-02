from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        groups = defaultdict(list)

        for t in transactions:
            name, time, amount, city = t.split(',')
            groups[name].append((int(time), int(amount), city, t))
        
        res = []

        for name, user_txns in groups.items():
            user_txns.sort(key = lambda x :x[0])

            n = len(user_txns)
            is_invalid = [False] * n

            for i in range(n):
                time_i, amount_i, city_i, raw_i = user_txns[i]

                if amount_i > 1000:
                    is_invalid[i] = True
                
                for j in range(i+1 , n):
                    time_j, amount_j, city_j, raw_j = user_txns[j]

                    if time_j - time_i > 60:
                        break
                    if city_i != city_j:
                        is_invalid[i] = True
                        is_invalid[j] = True
            
            for i in range(n):
                if is_invalid[i]:
                    res.append(user_txns[i][3])
        return res