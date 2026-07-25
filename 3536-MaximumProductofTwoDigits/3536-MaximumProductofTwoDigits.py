# Last updated: 7/26/2026, 1:45:56 AM
1class Solution:
2    def maxProduct(self, n: int) -> int:
3        max1 = max2 = 0
4        
5        while n > 0:
6            digit = n % 10
7            n //= 10
8            
9            if digit > max1:
10                max2 = max1
11                max1 = digit
12            elif digit > max2:
13                max2 = digit
14                
15        return max1 * max2