# Last updated: 7/12/2025, 11:43:24 PM
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # A triangle is valid only if the sum of any two sides is strictly greater than the third side.
        nums.sort()

        if (nums[0] + nums[1]) <= nums[2]: return "none"
        if (nums[0] == nums[2]): return "equilateral"
        if (nums[0] == nums[1] or nums[1] == nums[2]): return "isosceles"
        return "scalene"
