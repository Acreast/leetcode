# Last updated: 7/12/2025, 11:43:07 PM
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        ball_dict, color_dict = {}, {}
        distinct_count = 0

        for index, color in queries:
            if index in ball_dict:
                color_dict[ball_dict[index]] -= 1
                if color_dict[ball_dict[index]] == 0:
                    distinct_count -= 1
            ball_dict[index] = color
            color_dict[color] = color_dict.get(color, 0) + 1
            if color_dict[color] == 1: 
                distinct_count += 1
            res.append(distinct_count)
        
        return res