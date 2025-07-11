# Last updated: 7/12/2025, 11:45:14 PM
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        mat_to_position = {} # n -> (R, C)
        for r in range(ROWS):
            for c in range(COLS):
                mat_to_position[mat[r][c]] = (r, c)

        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        for i in range(len(arr)):
            r,c = mat_to_position[arr[i]] 
            row_cnt[r] += 1
            col_cnt[c] += 1

            if row_cnt[r] == COLS or col_cnt[c] == ROWS:
                return i