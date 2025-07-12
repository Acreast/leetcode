# Last updated: 7/12/2025, 11:50:16 PM
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        right_size = len(nums)
        prev = -1

        while (i < len(nums)):
            if (nums[i] == right_size) or (prev < right_size < nums[i]):
                return right_size
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            prev = nums[i]
            i += 1
            right_size = len(nums) - i
        
        return -1
