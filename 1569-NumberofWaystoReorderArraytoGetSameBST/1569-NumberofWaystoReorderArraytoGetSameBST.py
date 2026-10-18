# Last updated: 10/19/2026, 12:11:20 AM
1class Solution:
2    def numOfWays(self, nums: list[int]) -> int:
3        n = len(nums)
4        born = [-1] * (n + 2)
5        for t, x in enumerate(nums):
6            born[x] = t
7        
8        sizes, stack = 1, [0]
9        for v in range(1, n + 2):
10            while born[stack[-1]] > born[v]:
11                stack.pop()
12                sizes *= v - stack[-1] -1
13            stack.append(v)
14        
15        return (factorial(n) // sizes - 1) % (10 ** 9 + 7)