# Last updated: 7/12/2025, 11:50:27 PM
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        res = len(nums)
        cur_sum = 0
        cached = {
            0 : -1
        }

        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix =  (cur_sum - remainder + p) % p
            if prefix in cached:
                length = i - cached[prefix]
                res = min(res, length)
            cached[cur_sum] = i

        return -1 if res == len(nums) else res