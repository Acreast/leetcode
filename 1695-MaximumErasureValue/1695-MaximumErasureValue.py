# Last updated: 7/22/2025, 7:55:30 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        num_set = set()
        current_sum = 0
        for r in range(len(nums)):
            while nums[r] in num_set:
                current_sum -= nums[l]
                num_set.remove(nums[l])
                l += 1
            current_sum += nums[r]    
            num_set.add(nums[r])
            res = max(res, current_sum)
        return res
                