# Last updated: 1/12/2026, 12:24:38 AM
1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        if not matrix or not matrix[0]:
4            return 0
5        
6        M = len(matrix)
7        N = len(matrix[0])
8
9        for i in range(M):
10            for j in range(N):
11                matrix[i][j] = int(matrix[i][j])
12        
13        for i in range(M):
14            for j in range(1, N):
15                if matrix[i][j]  == 1:
16                    matrix[i][j] += matrix[i][j -1]
17        
18        res = 0 
19
20        for j in range(N):
21            for i in range(M):
22                width = matrix[i][j]
23                if width == 0:
24                    continue
25                
26                # Downwards expansion
27                cur_width = width
28                k = i
29                while k < M and matrix[k][j] > 0:
30                    cur_width = min(cur_width, matrix[k][j])
31                    height = k - i + 1
32                    res = max(res, cur_width * height)
33                    k += 1
34                
35                # Upwards expansion
36                cur_width = width
37                k = i
38                while k >= 0 and matrix[k][j] > 0:
39                    cur_width = min(cur_width, matrix[k][j])
40                    height = i - k + 1
41                    res = max(res, cur_width * height)
42                    k -= 1
43        
44        return res