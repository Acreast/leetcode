class Solution:
    def coloredCells(self, n: int) -> int:
        # Gauss formula logic:
        # 1 + the last number times the total count of n divided by two
        # Essentially half the number of (1 + last number) pairs
        return int(1+(4*(n - 1))/2 * n)