# Last updated: 7/12/2025, 11:48:23 PM
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        neg_count = 0
        matrix_min = float("inf")

        for row in matrix:
            for element in row:
                res += abs(element)
                matrix_min = min(matrix_min, abs(element))
                if element < 0:
                    neg_count += 1

        if neg_count % 2 != 0:
            res -= (matrix_min * 2)

        return res