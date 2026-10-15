# Last updated: 10/16/2026, 12:51:53 AM
1class Solution:
2    def sumCounts(self, nums: List[int]) -> int:
3        res = 0
4        for i in range(len(nums)):
5            distinct_elem = []
6            distinct = 0
7            for j in range(i, len(nums)):
8                if nums[j] not in distinct_elem:
9                    distinct_elem.append(nums[j])
10                    distinct += 1
11                res += distinct * distinct
12        return res
13                
14
15