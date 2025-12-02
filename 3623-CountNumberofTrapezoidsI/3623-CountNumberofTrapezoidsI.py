# Last updated: 12/3/2025, 7:13:44 AM
1class Solution:
2    def countTrapezoids(self, points: List[List[int]]) -> int:
3        freq=Counter(p[1] for p in points)
4        Sum, c2=0, 0
5        for f in freq.values():
6            if f<=1: continue
7            c=f*(f-1)//2
8            Sum+=c
9            c2+=c*c
10        return (Sum*Sum-c2)//2%(10**9+7)
11        