# Last updated: 7/12/2025, 11:42:33 PM
class Solution(object):
    def isZeroArray(self, nums, queries):
        diff = [0] * (len(nums) + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(nums):
                diff[r + 1] -= 1
        cnt = 0
        for i in range(len(nums)):
            cnt += diff[i]
            if nums[i] > cnt:
                return False
        return True