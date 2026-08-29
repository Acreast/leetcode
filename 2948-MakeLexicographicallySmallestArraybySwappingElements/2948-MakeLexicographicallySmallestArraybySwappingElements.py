# Last updated: 8/30/2026, 12:28:59 AM
1class Solution:
2    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
3        groups = []
4        num_to_groups = {}
5
6        for n in sorted(nums):
7            if not groups or abs(n - groups[-1][-1]) > limit:
8                groups.append(deque())
9
10            groups[-1].append(n)
11            num_to_groups[n] = len(groups) - 1
12
13        res = []
14
15        for n in nums:
16            j = num_to_groups[n]
17            res.append(groups[j].popleft())
18
19        return res