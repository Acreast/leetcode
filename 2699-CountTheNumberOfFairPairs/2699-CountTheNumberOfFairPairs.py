# Last updated: 7/12/2025, 11:45:04 PM
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin_search(l, r, target):
            while l <= r:
                m = l + ( r - l) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
                
            return r


        nums.sort()
        res = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                bin_search(i + 1, len(nums) - 1, up + 1) - 
                bin_search(i + 1, len(nums) - 1, low)
            )
            
        
        return res