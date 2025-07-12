# Last updated: 7/12/2025, 11:42:16 PM
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        count = len(startTime)
        prefixSum = [0] * (count + 1)
        max_time = 0

        for i in range(count):
            prefixSum[i + 1] = prefixSum[i] + (endTime[i] - startTime[i])
        
        for i in range(k -1, count):
            occupied = prefixSum[i + 1] - prefixSum[i - k + 1]
            window_end = eventTime if i == count - 1 else startTime[i + 1]
            window_start = 0 if i == k - 1 else endTime[i - k]
            free_time = window_end - window_start - occupied
            max_time = max(max_time, free_time)
        
        return max_time
