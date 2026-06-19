# Last updated: 6/20/2026, 1:26:48 AM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        res = 0
4        cur = 0
5        for n in gain:
6            cur += n
7            res = max(res, cur)
8        
9        return res