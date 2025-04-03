# Last updated: 4/4/2025, 12:10:58 AM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max = nums[0]
        max_diff = 0
        res = 0

        for n in range(1, len(nums)):
            res = max(res, max_diff * nums[n])
            prefix_max = max(prefix_max, nums[n])
            max_diff = max(max_diff, prefix_max - nums[n])
        
        return res
