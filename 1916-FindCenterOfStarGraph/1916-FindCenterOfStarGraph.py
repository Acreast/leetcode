# Last updated: 7/12/2025, 11:49:12 PM
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node_count = {}

        for u,v in edges:
            if u in node_count:
                node_count[u] += 1
            else:
                node_count[u] = 1
            
            if v in node_count:
                node_count[v] += 1
            else:
                node_count[v] = 1

        n = len(node_count)
        for node, count in node_count.items():
            if count == n - 1:
                return node

        return -1