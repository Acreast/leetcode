# Last updated: 7/12/2025, 11:49:22 PM
class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 1
        for i in range(1, N * 2):
            if nums[(i % N)] >= nums[(i - 1) % N]:
                count += 1
            else:
                count = 1
            if count == N:
                return True
        
        return N == 1