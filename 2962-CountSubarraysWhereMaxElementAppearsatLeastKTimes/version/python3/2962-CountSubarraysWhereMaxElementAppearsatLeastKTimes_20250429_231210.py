# Last updated: 4/29/2025, 11:12:10 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        occurence = 0
        res = 0
        left = 0
        for r in range(len(nums)):
            if nums[r] == maximum:
                occurence += 1
            while occurence >= k:
                if nums[left] == maximum:
                    occurence -= 1
                left += 1
            res += left
        return res