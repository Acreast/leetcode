# Last updated: 7/12/2025, 11:47:08 PM
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = Counter(nums)

        for num in nums:
            if nums[num] % 2 != 0:
                return False
        
        return True