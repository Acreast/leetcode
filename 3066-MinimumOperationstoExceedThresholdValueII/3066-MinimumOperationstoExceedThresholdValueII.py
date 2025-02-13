class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        
        while len(nums) > 1 and nums[0] < k:
            
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            res += 1
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
        
        return res
