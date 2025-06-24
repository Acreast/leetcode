# Last updated: 6/24/2025, 10:28:18 PM
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] != key:
                    continue
                if abs(i - j) <= k:
                    res.append(i)
                    break
        return res