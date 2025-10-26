# Last updated: 10/26/2025, 8:20:41 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_arr = []
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                target_arr = row
                break
        
        l = 0
        r = len(target_arr) - 1

        while l <= r:
            m = (l + r) // 2
            if target_arr[m] == target:
                return True
            if target_arr[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False