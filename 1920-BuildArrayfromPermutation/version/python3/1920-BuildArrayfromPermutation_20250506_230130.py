# Last updated: 5/6/2025, 11:01:30 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        for i in range(len(nums)):
            ans[i] = nums[i]
        
        for i in range(len(nums)):
            ans[i] = nums[ans[i]]
        return ans