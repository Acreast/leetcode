# Last updated: 1/14/2026, 12:28:16 AM
1class Solution:
2    def separateSquares(self, squares: List[List[int]]) -> float:
3        l = float('inf')
4        r = float('-inf')
5        total_area = 0
6        
7        for x, y, length in squares:
8            total_area += length * length
9            l = min(l, y)
10            r = max(r, y + length)
11
12        target_area = total_area / 2.0
13
14        for i in range(60):
15            mid = (l + r ) / 2.0
16
17            cur_area = 0
18            for _ , y, length in squares:
19                cur_y = max(0, min(length, mid - y))
20                cur_area += length * cur_y
21            
22            if cur_area < target_area:
23                l = mid
24            else:
25                r = mid
26        
27        return l
28
29            