# Last updated: 1/12/2026, 7:16:38 PM
1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        
4        cur_x, cur_y = points[0]
5        res = 0
6        for i in range(1,len(points)):
7            delta_x, delta_y = abs(points[i][0] - cur_x), abs(points[i][1] - cur_y)
8            offset = abs(delta_x - delta_y)
9            res += offset
10            res += min(delta_x, delta_y)
11            cur_x, cur_y = points[i][0], points[i][1]
12
13        return res
14
15            