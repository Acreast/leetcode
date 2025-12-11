# Last updated: 12/11/2025, 8:40:37 PM
1class Solution:
2    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
3        row = defaultdict(list)
4        col = defaultdict(list)
5        
6        for x, y in buildings:
7            row[x].append(y)
8            col[y].append(x)
9        
10        for r in row:
11            row[r].sort()
12        for c in col:
13            col[c].sort()
14        
15        res = 0
16        
17        for x, y in buildings:
18            ys = row[x]
19            pos = bisect.bisect_left(ys, y)
20            has_left = pos > 0
21            has_right = pos < len(ys) - 1
22            
23            xs = col[y]
24            pos2 = bisect.bisect_left(xs, x)
25            has_down = pos2 > 0
26            has_up = pos2 < len(xs) - 1
27            
28            if has_left and has_right and has_up and has_down:
29                res += 1
30        
31        return res
32