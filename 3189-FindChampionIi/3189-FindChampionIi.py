# Last updated: 7/12/2025, 11:43:52 PM
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n
        for src, dest in edges:
            incoming[dest] += 1
        
        champions = []
        for i, incoming_count in enumerate(incoming):
            if incoming_count == 0:
                champions.append(i)
        
        if len(champions) > 1:
            return -1
        
        return champions[0]