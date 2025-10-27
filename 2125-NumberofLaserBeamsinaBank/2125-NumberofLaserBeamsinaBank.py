# Last updated: 10/28/2025, 12:01:40 AM
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count("1")
        res = 0
        for i in range(1, len(bank)):
            cur =  bank[i].count("1")
            if cur > 0:
                res += prev * cur
                prev = cur
        return res