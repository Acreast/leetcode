# Last updated: 11/6/2026, 12:26:25 AM
1class Solution:
2    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
3        res = 0
4        invalid = False
5        for i in arr1:
6            for j in arr2:
7                if abs(i - j) <= d:
8                    invalid = True
9                    break
10            if invalid:
11                invalid = False
12                continue
13            res += 1
14        return res
15                
16                    
17