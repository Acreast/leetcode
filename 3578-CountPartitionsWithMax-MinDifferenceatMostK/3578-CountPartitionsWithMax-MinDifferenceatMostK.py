# Last updated: 12/7/2025, 12:07:03 AM
1class Solution:
2    def countPartitions(self, nums, k):
3        n = len(nums)
4        MOD = 10**9 + 7
5        
6        dp = [0] * (n + 1)
7        dp[0] = 1
8        
9        from collections import deque
10        mx, mn = deque(), deque()
11        
12        l = 0
13        s = 0
14        
15        for r in range(n):
16            while mx and nums[mx[-1]] <= nums[r]:
17                mx.pop()
18            while mn and nums[mn[-1]] >= nums[r]:
19                mn.pop()
20            mx.append(r)
21            mn.append(r)
22            
23            while nums[mx[0]] - nums[mn[0]] > k:
24                if mx[0] == l:
25                    mx.popleft()
26                if mn[0] == l:
27                    mn.popleft()
28                s = (s - dp[l]) % MOD
29                l += 1
30            
31            s = (s + dp[r]) % MOD
32            dp[r + 1] = s
33        
34        return dp[n]
35