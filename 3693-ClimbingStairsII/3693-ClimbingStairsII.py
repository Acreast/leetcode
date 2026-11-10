# Last updated: 11/10/2026, 9:22:27 PM
1class Solution:
2    def climbStairs(self, n: int, costs: list[int]) -> int:
3        costs = [0] + costs  # step 0 is free, step i costs costs[i]
4
5        @cache
6        def climb(i: int = 0) -> int:  # cheapest way from i to n
7            if i > n:
8                return inf  # jumped past the top
9            if i == n:
10                return costs[n]  # on top: just pay for it
11            return costs[i] + min(climb(i + 1) + 1, climb(i + 2) + 4, climb(i + 3) + 9)
12
13        return climb()