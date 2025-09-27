# Last updated: 9/27/2025, 10:42:24 PM
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    first_x, first_y = points[i]
                    second_x, second_y = points[j]
                    third_x, third_y = points[k]
                    area = (0.5 * abs(
                        first_x * (second_y - third_y) +
                        second_x * (third_y - first_y) + 
                        third_x * (first_y - second_y)
                    ))

                    res = max(res, area)
        return res

                    