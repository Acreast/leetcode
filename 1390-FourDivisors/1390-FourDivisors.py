# Last updated: 1/5/2026, 12:28:15 AM
1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3        # Case 1: p^3
4        # Case 2: p×q (Where p and q are two distinct primes)
5        res = 0
6        for n in nums:
7            val = self.sumOne(n)
8            if val != -1:
9                res += val
10        return res
11
12    def sumOne(self, n:int) -> int:
13        prime = round(n ** (1/3))
14        if prime ** 3 == n  and self.isPrime(prime):
15            return 1 + prime + prime*prime + prime*prime*prime
16        
17        for i in range(2, int(n ** 0.5) + 1):
18            if n % i == 0:
19                a, b = i, n // i
20                if a != b and self.isPrime(a) and self.isPrime(b):
21                    return 1 + a + b + n
22                return -1
23        return -1
24
25    def isPrime(self, x: int) -> bool:
26        if x < 2:
27            return False
28        for i in range(2, int(x ** 0.5) + 1):
29            if x % i == 0:
30                return False
31        return True