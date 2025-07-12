# Last updated: 7/12/2025, 11:48:12 PM
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        pointer = 0
        res = []
        if m * n != len(original):
            return []
        
        for rows in range(m):
            row_arr = []
            for cols in range(n):
                row_arr.append(original[pointer])
                pointer += 1
            res.append(row_arr)
        
        return res
