# Last updated: 7/12/2025, 11:47:59 PM
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        events.sort(key=lambda x: x[0])

        suffix_max = n * [0]
        suffix_max[n-1] = events[n-1][2]

        for i in range(n-2,-1,-1):
            suffix_max[i] = max(events[i][2], suffix_max[i + 1])
        
        max_sum = 0

        for i in range(n):
            left, right = i + 1, n - 1
            next_event_index = -1
        
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    next_event_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            if next_event_index != -1:
                max_sum = max(max_sum, events[i][2] + suffix_max[next_event_index])
            
            max_sum = max(max_sum, events[i][2])
        
        return max_sum