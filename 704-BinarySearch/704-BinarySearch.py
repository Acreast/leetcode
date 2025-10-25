# Last updated: 10/25/2025, 9:04:12 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1