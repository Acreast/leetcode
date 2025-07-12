# Last updated: 7/12/2025, 11:43:28 PM
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        values = nums.copy()

        for i in range(n):
            for j in range(n - i - 1):
                if values[j] <= values[j+1]:
                    continue
                if bin(values[j]).count("1") == bin(values[j + 1]).count("1"):
                    values[j], values[j + 1] = values[j + 1], values[j]
                else:
                    return False
        
        return True
