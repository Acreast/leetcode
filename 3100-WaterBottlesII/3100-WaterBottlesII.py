# Last updated: 10/3/2025, 12:33:07 AM
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            numExchange += 1
            res += 1
        return res
