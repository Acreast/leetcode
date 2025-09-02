# Last updated: 9/3/2025, 1:40:14 AM
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        n = len(points)

        for i in range(n):
            upper_y = points[i][1]
            lower_y_limit = float('-inf')

            for j in range(i + 1, n):
                current_y = points[j][1]
                if current_y <= upper_y and current_y > lower_y_limit:
                    res += 1
                    lower_y_limit = current_y
                    if current_y == upper_y:
                        break
        return res