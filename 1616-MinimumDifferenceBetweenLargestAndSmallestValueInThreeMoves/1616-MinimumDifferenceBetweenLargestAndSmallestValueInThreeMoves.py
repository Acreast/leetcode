# Last updated: 7/12/2025, 11:50:53 PM
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        res = float("inf")
        for l in range(4):
            r = len(nums) - 4 + l
            res = min(
                res,
                nums[r] - nums[l]
            )
        
        return res
