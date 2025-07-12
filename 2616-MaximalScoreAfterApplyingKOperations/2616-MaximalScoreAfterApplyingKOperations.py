# Last updated: 7/12/2025, 11:45:29 PM
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0


        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        while k:
            num = -heapq.heappop(max_heap)
            res += num
            k -= 1
            heapq.heappush(max_heap, -math.ceil(num/3))

        return res