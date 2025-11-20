# Last updated: 11/21/2025, 12:01:30 AM
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key = lambda x:(x[1], - x[0]))
        p1, p2 = -1, -1

        for left, right in intervals:
            if p2 < left:
                res += 2
                p1, p2 = right - 1, right
            elif p1 < left:
                res += 1
                p1, p2 = p2, right
            
        
        return res