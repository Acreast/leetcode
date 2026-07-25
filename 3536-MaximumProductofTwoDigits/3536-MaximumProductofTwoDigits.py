# Last updated: 7/26/2026, 1:44:23 AM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        num_arr = []
4        for c in str(n):
5            num_arr.append(c)
6        
7        num_arr.sort()
8
9        return int(num_arr[-1]) * int(num_arr[-2])