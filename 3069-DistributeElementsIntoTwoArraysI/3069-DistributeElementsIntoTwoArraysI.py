# Last updated: 8/21/2026, 12:32:07 AM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        arr1 = [nums[0]]
4        arr2 = [nums[1]]
5        
6        for i in range(2, len(nums)):
7            if arr1[-1] > arr2[-1]:
8                arr1.append(nums[i])
9            else:
10                arr2.append(nums[i])
11
12        return arr1 + arr2
13
14