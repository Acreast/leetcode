# Last updated: 7/12/2025, 11:54:46 PM
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float("inf")
        
        pairs = []
        for i in range (len(quality)):
            pairs.append((wage[i]/quality[i], quality[i]))
        pairs.sort(key=lambda p:p[0])

        maxHeap = []
        total_quality = 0
        for rate, quality in pairs:
            heapq.heappush(maxHeap, -quality)
            total_quality += quality

            if (len(maxHeap) > k):
                total_quality += heapq.heappop(maxHeap)

            if (len(maxHeap) == k):
                res = min(res, total_quality * rate)

        return res