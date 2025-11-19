# Last updated: 11/19/2025, 8:27:07 PM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while True:
            if original in nums:
                original = 2 * original
            else:
                break

        return original