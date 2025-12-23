# Last updated: 12/24/2025, 1:43:44 AM
1class Solution:
2    def maxTwoEvents(self, events: List[List[int]]) -> int:
3        n = len(events)
4
5        events.sort(key=lambda x: x[0])
6
7        suffix_max = n * [0]
8        suffix_max[n-1] = events[n-1][2]
9
10        for i in range(n-2,-1,-1):
11            suffix_max[i] = max(events[i][2], suffix_max[i + 1])
12        
13        max_sum = 0
14
15        for i in range(n):
16            left, right = i + 1, n - 1
17            next_event_index = -1
18        
19            while left <= right:
20                mid = left + (right - left) // 2
21                if events[mid][0] > events[i][1]:
22                    next_event_index = mid
23                    right = mid - 1
24                else:
25                    left = mid + 1
26            
27            if next_event_index != -1:
28                max_sum = max(max_sum, events[i][2] + suffix_max[next_event_index])
29            
30            max_sum = max(max_sum, events[i][2])
31        
32        return max_sum