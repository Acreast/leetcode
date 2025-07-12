# Last updated: 7/12/2025, 11:49:03 PM
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        mask = 2 ** maximumBit - 1
        result = []
        for n in reversed(nums):
            result.append(xor ^ mask)
            xor ^= n
        
        return result

