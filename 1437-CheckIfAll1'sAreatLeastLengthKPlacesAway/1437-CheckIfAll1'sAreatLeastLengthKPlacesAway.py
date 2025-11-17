# Last updated: 11/17/2025, 6:56:08 PM
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cons = k
        for n in nums:
            if n == 0:
                cons += 1
            else:
                if cons < k:
                    return False
                cons = 0

        return True