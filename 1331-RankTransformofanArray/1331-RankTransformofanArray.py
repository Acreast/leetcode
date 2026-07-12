# Last updated: 7/13/2026, 12:09:06 AM
1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        value_to_rank = {}
4        sorted_arr = sorted(list(set(arr)))
5
6        for index in range(len(sorted_arr)):
7            value_to_rank[sorted_arr[index]] = index + 1
8        
9        for index in range(len(arr)):
10            arr[index] = value_to_rank[arr[index]]
11        
12        return arr