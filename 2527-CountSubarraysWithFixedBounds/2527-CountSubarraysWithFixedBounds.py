# Last updated: 7/12/2025, 11:46:01 PM
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