# Last updated: 12/15/2025, 8:42:55 PM
1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        res = 0
4        consecutive_desc_len = 1
5
6        for i in range(1, len(prices)):
7            if prices[i] == prices[i - 1] - 1:
8                consecutive_desc_len += 1
9            else:
10                res += consecutive_desc_len * (consecutive_desc_len + 1) // 2
11                consecutive_desc_len = 1
12
13        res += consecutive_desc_len * (consecutive_desc_len + 1) // 2
14
15        return res
16
17            
18            
19
20