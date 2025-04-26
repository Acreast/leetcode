# Last updated: 4/26/2025, 10:12:49 PM
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        l = -1
        minimum = -1
        maximum = -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                l = i
            if nums[i] == maxK:
                maximum = i
            if nums[i] == minK:
                minimum = i
            valid = max(0, min(minimum, maximum) - l)
            res += valid

        return res