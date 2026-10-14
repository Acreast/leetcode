# Last updated: 10/14/2026, 11:17:38 PM
1class Solution:
2    def maxSumOfSquares(self, num: int, sum: int) -> str:
3        if sum > 9 * num: return "" 
4        nines, rest = divmod(sum, 9)
5        return ("9" * nines + str(rest) + "0" * num)[:num]  