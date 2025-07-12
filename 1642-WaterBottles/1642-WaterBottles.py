# Last updated: 7/12/2025, 11:50:42 PM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drank = 0
        while numBottles > 0:
            drank += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        
        return drank