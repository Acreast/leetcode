# Last updated: 8/25/2025, 11:37:47 PM
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        ROWS = len(mat)
        COLS = len(mat[0])
        res = []
        y = 0
        x = 0
        for _ in range(ROWS * COLS):
            res.append(mat[x][y])
            
            if (x + y) % 2 == 0:
                if y == COLS - 1:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    x -= 1
                    y += 1
            else:
                if x == ROWS - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1
        return res
                