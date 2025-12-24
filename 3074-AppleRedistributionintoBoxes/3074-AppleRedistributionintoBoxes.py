# Last updated: 12/24/2025, 2:33:44 PM
1class Solution:
2    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
3        capacity.sort(reverse=True)
4        apple_sum = sum(apple)
5        count = 0
6        for c in capacity:
7            apple_sum -= c
8            count += 1
9            if apple_sum <= 0:
10                return count
11        
12        return count
13
14