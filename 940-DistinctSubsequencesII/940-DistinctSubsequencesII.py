# Last updated: 9/7/2026, 11:52:21 PM
1class Solution:
2    MOD = 10 ** 9 + 7
3    def distinctSubseqII(self, s: str) -> int:
4        res = 0
5        dp = [0] * 26
6
7        for c in s:
8            c = ord(c) - 97
9            new = res + 1 - dp[c]
10            res = (res + new) % self.MOD
11            dp[c] = (dp[c] + new ) % self.MOD
12        
13        return res