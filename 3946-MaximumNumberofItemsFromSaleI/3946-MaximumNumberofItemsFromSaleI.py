# Last updated: 11/27/2026, 11:38:59 PM
1class Solution:
2    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
3        factors, prices = zip(*items)
4        have = [0] * (max(factors) + 1)
5        for factor in factors:
6            have[factor] += 1
7        gains = {factor: sum(have[factor::factor]) for factor in set(factors)}  # every factor-th cell is a multiple
8
9        cheapest = min(prices)
10        best = [money // cheapest for money in range(budget + 1)]  # no first copies yet: everything goes to the cheapest item
11        for factor, price in items:
12            if (gain := gains[factor]) > price // cheapest:  # else the same money buys as many copies of the cheapest item
13                for money in range(budget, price - 1, -1):  # backwards: one first copy per item
14                    best[money] = max(best[money], best[money - price] + gain)
15        return best[budget]