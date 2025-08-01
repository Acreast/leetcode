# Last updated: 7/12/2025, 11:43:39 PM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            res.append(nums[i:i+3])
        return res