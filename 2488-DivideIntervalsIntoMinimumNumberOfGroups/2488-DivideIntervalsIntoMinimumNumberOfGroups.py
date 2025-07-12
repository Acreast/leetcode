# Last updated: 7/12/2025, 11:46:16 PM
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []

        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        i = 0
        j = 0
        groups = 0
        res = 0
        while i < len(intervals):
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                groups -= 1
                j += 1
            res = max(res, groups)

        return res