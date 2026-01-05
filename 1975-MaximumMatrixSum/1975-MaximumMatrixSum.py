# Last updated: 1/6/2026, 1:25:05 AM
1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        res = 0
4        neg_count = 0
5        min_tracker = float("inf")
6
7        for row in matrix:
8            for element in row:
9                res += abs(element)
10                min_tracker = min(min_tracker, abs(element))
11                if element < 0:
12                    neg_count += 1
13                
14        if neg_count % 2 != 0:
15            res -= min_tracker * 2
16                
17
18        return res