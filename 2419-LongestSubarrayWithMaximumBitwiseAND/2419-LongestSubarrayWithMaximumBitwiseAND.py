# Last updated: 7/30/2025, 9:04:45 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        last_num = None
        counter = 1
        res = 1
        for n in nums:
            if n == target and last_num == target:
                counter += 1
                res = max(counter, res)
            else:
                counter = 1
            last_num = n
        return res