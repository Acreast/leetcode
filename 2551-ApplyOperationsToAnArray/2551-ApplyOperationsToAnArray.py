# Last updated: 7/12/2025, 11:45:54 PM
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1 ):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        
        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        
        return nums