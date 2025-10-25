# Last updated: 10/25/2025, 3:17:14 PM
class Solution:
    def totalMoney(self, n: int) -> int:
        nth_day = 0
        res = 0
        weeks = n // 7
        remainder = n % 7

        if weeks == 0:
            for i in range(1, 7):
                res += i
                if i == n:
                    return res
            return res

        for w in range(weeks):
            for i in range(1, 8):
                res += i + w
                nth_day += 1
                if nth_day == n:
                    return res

        if remainder:
            for i in range(1, remainder + 1):
                res += i + weeks

        return res