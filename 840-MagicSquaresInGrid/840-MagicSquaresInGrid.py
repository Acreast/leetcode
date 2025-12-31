# Last updated: 12/31/2025, 9:29:48 PM
1class Solution:
2    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
3        def canCross(day):
4            grid = [[0] * col for _ in range(row)]
5            
6            for i in range(day):
7                r, c = cells[i][0] - 1, cells[i][1] - 1
8                grid[r][c] = 1
9
10            queue = deque()
11            visited = [[False] * col for _ in range(row)]
12            
13            for c in range(col):
14                if grid[0][c] == 0:
15                    queue.append((0, c))
16                    visited[0][c] = True
17
18            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
19
20            while queue:
21
22                r , c = queue.popleft()
23                if r == row - 1:
24                    return True
25                
26                for dr, dc in neighbors:
27                    nr, nc = r + dr, c + dc
28                    
29                    if 0 <= nr < row and 0 <= nc < col and \
30                       not visited[nr][nc] and grid[nr][nc] == 0:
31                        visited[nr][nc] = True
32                        queue.append((nr, nc))
33            return False
34
35        res = 0
36
37        l = 1
38        r = len(cells)
39
40        while l <= r:
41            day = (l + r) // 2
42
43            if canCross(day):
44                res = day
45                l = day + 1
46            else:
47                r = day - 1
48        
49        return res