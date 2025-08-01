# Last updated: 7/12/2025, 11:42:37 PM
class Solution:
    MOD = 10**9 + 7
    def powerMatrix(self, matrix, exponent):
            n = len(matrix)
            result = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
            while exponent > 0:
                if exponent & 1:
                    result = self.multiplyMatrices(result, matrix)
                matrix = self.multiplyMatrices(matrix,matrix)
                exponent >>= 1
            return result
        
    def multiplyMatrices(self, A, B):
        rowsA, colsA, colsB = len(A), len(A[0]), len(B[0])
        result = [[0]*colsB for _ in range(rowsA)]
        for i in range(rowsA):
            for j in range(colsB):
                tmp = 0
                for k in range(colsA):
                    tmp += A[i][k] * B[k][j]
                result[i][j] = tmp % self.MOD
        return result

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        transform = [[0]*26 for _ in range(26)]
        for i in range(26):
            for shift in range(nums[i]):
                transform[i][(i + 1 + shift) % 26] += 1
        transform = self.powerMatrix(transform, t)
        freq = [[0]*26]
        for ch in s:
            freq[0][ord(ch) - ord('a')] += 1
        freq = self.multiplyMatrices(freq, transform)
        return sum(freq[0]) % self.MOD
        
