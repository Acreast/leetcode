# Last updated: 10/23/2026, 12:45:58 AM
1class Solution:
2    def minOperations(self, A: List[int]) -> int:
3        n = len(A)
4        asc = dsc = 1
5        for i in range(1, n):
6            asc += A[i] == (A[i - 1] + 1) % n
7            dsc += A[i - 1] == (A[i] + 1) % n
8        
9        if asc == n:
10            return 0 if not A[0] else min(n - A[0], A[0] + 2)
11        
12        if dsc == n:
13            return min(n - A[-1], A[-1]) + 1
14
15        return -1