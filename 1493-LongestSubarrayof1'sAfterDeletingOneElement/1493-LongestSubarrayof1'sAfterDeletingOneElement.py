# Last updated: 8/24/2025, 1:45:29 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last_chain = 0
        res = 0
        cur_chain = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                res = max((last_chain + cur_chain), res)
                last_chain = cur_chain
                cur_chain = 0
                continue
            else:
                cur_chain += 1
            
            if i == len(nums) - 1:
                if cur_chain:
                    res = max((last_chain + cur_chain), res)

        if last_chain == 0 and cur_chain == len(nums):
            return len(nums) - 1

        return res