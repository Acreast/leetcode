# Last updated: 7/12/2025, 11:43:08 PM
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = 0

        for start, end in meetings:
            start = max(prev_end + 1, start)
            length = end - start + 1
            days -= max(length ,0)
            prev_end = max(prev_end, end)
        
        return days