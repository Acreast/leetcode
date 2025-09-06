# Last updated: 9/6/2025, 10:56:24 PM
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def helper(num):
            if num <= 0:
                return 0
            if num <= 3:
                return num
            res = 0
            base = 1
            step = 1

            while base <= num:
                count = min(num, base * 4 - 1) - base + 1
                res += count * step
                base *= 4
                step += 1
            return res


        res = 0
        for l, r in queries:
            total = helper(r) - helper(l-1)
            res += (total + 1) // 2
        return res