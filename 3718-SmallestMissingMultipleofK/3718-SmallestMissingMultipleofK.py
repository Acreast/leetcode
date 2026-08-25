# Last updated: 8/25/2026, 8:41:12 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        n = 1
4        nums.sort()
5        for num in nums:
6            if k * n < num:
7                continue
8            if k * n == num:
9                n += 1
10                continue
11            if k * n < num:
12                return k * n
13        
14        return k * n
15
16        
17