# Last updated: 7/12/2025, 11:48:36 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        for i in range(len(nums)):
            ans[i] = nums[i]
        
        for i in range(len(nums)):
            ans[i] = nums[ans[i]]
        return ans