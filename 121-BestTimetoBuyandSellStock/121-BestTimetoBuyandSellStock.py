class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 0
        res = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                res = max((prices[r] - prices[l]), res)    
            else:
                l = r

            r += 1
        
        return res