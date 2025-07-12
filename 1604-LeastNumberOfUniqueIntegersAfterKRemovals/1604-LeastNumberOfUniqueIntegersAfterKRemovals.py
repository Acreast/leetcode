# Last updated: 7/12/2025, 11:51:04 PM
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)

        res = len(heap)
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
        return res