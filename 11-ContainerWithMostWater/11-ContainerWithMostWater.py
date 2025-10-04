# Last updated: 10/5/2025, 1:36:18 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        # for l in range(len(height)):
        #     r = len(height) - 1
        #     while r > l:
        #         res = max(min(height[l], height[r]) * (r - l), res)
        #         r -= 1
        r = len(height) - 1
        l = 0
        while l < r:
            current_size = min(height[l], height[r]) * (r - l)
            res = max(res, current_size)
            if height[l] <  height[r]:
                l+= 1
            else:
                r -= 1
        return res
            

