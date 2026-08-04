# Last updated: 8/4/2026, 11:17:07 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        nums.sort()
4        res = []
5        for i in range(len(nums) - 1):
6            if nums[i + 1] != nums[i] + 1:
7                cur = nums[i] + 1
8                while cur != nums[i + 1]:
9                    res.append(cur)
10                    cur += 1
11        return res
12