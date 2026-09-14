# Last updated: 9/14/2026, 10:13:13 PM
1class Solution:
2    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
3        x_overlap = min(rec1[2],rec2[2]) > max(rec1[0],rec2[0])
4        y_overlap = min(rec1[3],rec2[3]) > max(rec1[1],rec2[1])
5        return x_overlap and y_overlap
6
7