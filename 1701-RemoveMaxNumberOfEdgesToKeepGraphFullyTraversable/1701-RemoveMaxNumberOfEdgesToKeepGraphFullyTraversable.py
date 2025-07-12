# Last updated: 7/12/2025, 11:50:24 PM
class UF:
    def __init__(self,n_of_components):
        self.n_of_components = n_of_components
        self.parent = [i for i in range(n_of_components + 1)]
        self.rank = [1] * (n_of_components + 1)

    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.n_of_components -=1
        return 1

    def is_connected(self):
        return self.n_of_components <= 1 

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UF(n), UF(n)
        cnt = 0

        for t, src, dest in edges:
            if t == 3:
                cnt += (alice.union(src,dest) | bob.union(src,dest))
        
        for t, src, dest in edges:
            if t == 1:
                cnt += alice.union(src,dest)
            elif t == 2:
                cnt += bob.union(src,dest)

        if bob.is_connected() and alice.is_connected():
            return len(edges) - cnt
        
        return -1