# Last updated: 11/25/2025, 9:33:26 PM
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cur = 1
        res = 1
        seen = set()
        while cur % k:
            if cur in seen:
                return - 1
            seen.add(cur)
            cur = 10 * (cur % k) + 1
            res += 1

        return res