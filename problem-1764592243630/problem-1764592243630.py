# Last updated: 12/1/2025, 8:30:43 PM
1class Solution:
2    def maxRunTime(self, n: int, batteries: List[int]) -> int:
3        
4        batteries.sort()
5        total = sum(batteries)
6        while batteries[-1] > total // n:
7            n -= 1
8            total -= batteries.pop()
9        return total // n