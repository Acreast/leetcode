# Last updated: 6/29/2025, 7:56:20 PM
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        r = len(nums) - 1
        MOD = 10** 9 + 7
        for i, l in enumerate(nums):
            while (nums[r] + l) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2 ** ( r - i))
                res %= MOD

        return res
        