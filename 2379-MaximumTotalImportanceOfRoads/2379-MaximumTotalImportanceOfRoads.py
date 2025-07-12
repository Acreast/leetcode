# Last updated: 7/12/2025, 11:46:53 PM
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_cnt = [0] * n

        for e1, e2 in roads:
            edge_cnt[e1] += 1
            edge_cnt[e2] += 1
        
        label = 1
        res = 0 
        for count in sorted(edge_cnt):
            res += count * label
            label += 1
        
        return res