# Last updated: 12/19/2025, 10:41:55 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        q = deque()
4        res = []
5        l = r = 0
6
7        while r < len(nums):
8            while q and nums[q[-1]] < nums[r]:
9                q.pop()    
10            q.append(r)
11
12            if l > q[0]:
13                q.popleft()
14            
15            if (r + 1) >= k:
16                res.append(nums[q[0]])
17                l += 1
18
19            r += 1
20        
21        return res
22