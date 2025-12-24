# Last updated: 12/24/2025, 11:37:05 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3
4        nums.sort()
5        for i in range(len(nums) - 1):
6                if nums[i] == nums[i + 1]:
7                    return nums[i]
8        