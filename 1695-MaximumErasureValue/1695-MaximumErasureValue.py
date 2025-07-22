# Last updated: 7/22/2025, 8:25:32 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 0
        num_set = set()
        cur_sum = 0
        for r in range(len(nums)):
            while nums[r] in num_set:
                cur_sum -= nums[l]
                num_set.remove(nums[l])
                l += 1
            
            cur_sum += nums[r]
            num_set.add(nums[r])
            res = max(cur_sum, res)
        return res        