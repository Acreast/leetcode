# Last updated: 7/12/2025, 11:46:57 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        res = 0

        for i in range(len(nums) -1):
            right -= nums[i]
            left += nums[i]

            if left >= right:
                res +=1
        
        return res