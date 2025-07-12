# Last updated: 7/12/2025, 11:51:03 PM
class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res