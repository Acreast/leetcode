# Last updated: 7/12/2025, 11:52:51 PM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}
        sorted_arr = sorted(list(set(arr)))

        for index in range(len(sorted_arr)):
            value_to_rank[sorted_arr[index]] = index + 1
        
        for index in range(len(arr)):
            arr[index] = value_to_rank[arr[index]]
        
        return arr