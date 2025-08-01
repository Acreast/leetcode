# Last updated: 7/12/2025, 11:44:37 PM
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(v, res):
            if v in visited:
                return 
            visited.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei, res)
            return res
        
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        res = 0
        visited = set()
        for v in range(n):
            if v in visited:
                continue
            
            component = dfs(v, [])
            flag = True
            for v2 in component:
                if len(component) - 1 != len(adj[v2]):
                    flag = False
                    break
            if flag:
                res += 1


        return res