# Last updated: 12/9/2025, 7:51:06 PM
1class Solution:
2    def specialTriplets(self, nums: List[int]) -> int:
3        right_counter = Counter(nums[2:])
4        left_counter = Counter([nums[0]])
5        MOD = 10**9 + 7
6        res = 0
7        for j in range(1, len(nums) - 1):
8            target = nums[j] * 2
9            if target in right_counter:
10                res = (res + left_counter[target] * right_counter[target]) % MOD
11            right_counter[nums[j + 1]] -= 1
12            if right_counter[nums[j]] == 0:
13                del right_counter[nums[j]]
14            left_counter[nums[j]] += 1
15        
16        return res
17        
18
19            