# Last updated: 7/12/2025, 11:42:54 PM
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[num + 1] for num in range(n)]

        def shortest_path():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))
            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)


        res = []

        for src, dest in queries:
            adj[src].append(dest)
            res.append(shortest_path())

        return res