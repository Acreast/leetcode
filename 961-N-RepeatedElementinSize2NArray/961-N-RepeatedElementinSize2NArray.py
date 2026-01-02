# Last updated: 1/2/2026, 8:27:38 PM
1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        n2 = len(nums) // 2
4        nums.sort()
5        prev = -1
6        counter = 1
7        for n in nums:
8            if n == prev:
9                counter += 1
10            else:
11                counter = 1
12                prev = n
13            if counter == n2:
14                return n
15        return 0
16
17