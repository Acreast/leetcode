# Last updated: 11/16/2025, 10:48:06 PM
class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        cons = 0
        MOD = 10 ** 9 + 7
        for c in s:
            if c == "1":
                cons += 1
                res += cons
            else:
                cons = 0

        return res % MOD