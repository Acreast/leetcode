# Last updated: 8/31/2026, 12:53:03 AM
1class Solution:
2    def minimumDeletions(self, nums: List[int]) -> int:
3        n = len(nums)
4        left = 0
5        right = 0
6        
7        for i in range(1, n):
8            if nums[i] < nums[left]:
9                left = i
10                
11            if nums[i] > nums[right]:
12                right = i
13                
14        if left < right:
15            left, right = right, left
16            
17        ans = n
18        
19        for i in range(n + 1):
20            extra = 0
21            
22            if right >= i:
23                extra = n - right
24            elif left >= i:
25                extra = n - left
26                
27            ans = min(ans, i + extra)
28            
29        return ans