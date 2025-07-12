# Last updated: 7/12/2025, 11:53:20 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_height = sorted(heights)

        res = 0
        for i in range(len(heights)):
            if expected_height[i] != heights[i]:
                res += 1
        
        return res