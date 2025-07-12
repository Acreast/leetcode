# Last updated: 7/12/2025, 11:51:07 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [p for p in prices]

        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]  
            stack.append(i)
        return res