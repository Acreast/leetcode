# Last updated: 7/12/2025, 11:42:35 PM
class Solution:
    def buildList(self, edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
    def dfs(self, adj, u, p, k):
        if k < 0:
            return 0
        count = 1
        for v in adj[u]:
            if v != p:
                count += self.dfs(adj, v, u, k - 1 )
        return count

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adj1 = self.buildList(edges1)
        adj2 = self.buildList(edges2)
        max_of_b = 0
        for i in range(len(adj2)):
            max_of_b = max(max_of_b, self.dfs(adj2, i, -1, k -1))
        res = []
        for i in range(len(adj1)):
            res.append(self.dfs(adj1, i, -1 ,k) + max_of_b)
        return res
            
