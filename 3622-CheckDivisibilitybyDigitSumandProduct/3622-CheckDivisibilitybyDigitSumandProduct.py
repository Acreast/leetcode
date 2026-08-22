# Last updated: 8/23/2026, 1:21:18 AM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        original = n 
4        digit_sum = 0
5        digit_product = 1
6
7        while n > 0:
8            digit = n % 10
9            digit_sum += digit
10            digit_product *= digit
11            n //= 10
12        
13        divisor = digit_sum + digit_product
14        return original % divisor == 0