# Last updated: 7/12/2025, 11:42:26 PM
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]

        x.sort()
        y.sort()
        
        def count_overlapping(intervals):
            prev_end = -1
            count = 0
            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)

            return count

        
        return max(
            count_overlapping(x),
            count_overlapping(y)
        ) >= 3
        

