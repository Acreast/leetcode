# Last updated: 4/8/2025, 11:02:45 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_map = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in num_map:
                return i // 3 + 1
            num_map.add(nums[i])
        return 0