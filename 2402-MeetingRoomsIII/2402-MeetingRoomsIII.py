# Last updated: 12/28/2025, 1:34:39 AM
1class Solution:
2    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
3        room_availability_time = [0] * n
4        meeting_count = [0] * n
5        for start, end in sorted(meetings):
6            min_room_availability_time = inf
7            min_available_time_room = 0
8            found_unused_room = False
9            for i in range(n):
10                if room_availability_time[i] <= start:
11                    found_unused_room = True
12                    meeting_count[i] += 1
13                    room_availability_time[i] = end
14                    break
15                if min_room_availability_time > room_availability_time[i]:
16                    min_room_availability_time = room_availability_time[i]
17                    min_available_time_room = i
18            if not found_unused_room:
19                room_availability_time[min_available_time_room] += end - start
20                meeting_count[min_available_time_room] += 1
21
22        return meeting_count.index(max(meeting_count))