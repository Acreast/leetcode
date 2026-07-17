# Last updated: 7/18/2026, 1:33:40 AM
1class Solution:
2    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
3        max_num = max(nums)
4        freq = [0] * (max_num + 1)
5        for num in nums:
6            freq[num] += 1
7        
8        GCD = [0] * (max_num + 1)
9
10        for i in range(max_num, 0, -1):
11            total = sum(freq[i::i])
12            GCD[i] = total * (total - 1) // 2 - sum(GCD[i::i])
13        
14        GCD = list(accumulate(GCD))
15
16        return [bisect.bisect_right(GCD, q) for q in queries]