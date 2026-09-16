# Last updated: 9/16/2026, 11:02:19 PM
1class Solution:
2    MOD = 10**9 + 7
3
4    def mod_pow(self, base: int, exp: int) -> int:
5        result = 1
6
7        while exp > 0:
8            if exp & 1:
9                result = result * base % self.MOD
10
11            base = base * base % self.MOD
12
13            exp >>= 1
14
15        return result
16
17    def numberOfSets(self, n: int, k: int) -> int:
18        N = n + k - 1
19        R = 2 * k
20
21        R = min(R, N - R)
22
23        numerator = 1
24        denominator = 1
25
26        for i in range(1, R + 1):
27            numerator = numerator * (N - R + i) % self.MOD
28
29            denominator = denominator * i % self.MOD
30
31        inverse_denominator = self.mod_pow(
32            denominator,
33            self.MOD - 2
34        )
35
36        return numerator * inverse_denominator % self.MOD