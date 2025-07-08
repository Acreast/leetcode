# Last updated: 7/8/2025, 9:53:04 PM
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day= max(event[1] for event in events)
        events.sort()
        pq = []
        res, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                res += 1
        return res
            