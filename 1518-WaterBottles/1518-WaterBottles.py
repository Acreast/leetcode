# Last updated: 10/1/2025, 11:38:22 PM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        res = 0
        while numBottles > 0:
            res += numBottles
            empty += numBottles
            numBottles = empty // numExchange 
            empty = empty % numExchange
        
        return res