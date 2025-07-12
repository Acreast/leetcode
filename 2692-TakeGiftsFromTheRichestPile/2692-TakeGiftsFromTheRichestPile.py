# Last updated: 7/12/2025, 11:45:08 PM
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(n)))

        return -sum(gifts)