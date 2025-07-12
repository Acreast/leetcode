# Last updated: 7/12/2025, 11:45:59 PM
class Solution:
    def minimizeArrayValue(self, A: List[int]) -> int:
        return max((a + i) // (i + 1) for i,a in enumerate(accumulate(A)))