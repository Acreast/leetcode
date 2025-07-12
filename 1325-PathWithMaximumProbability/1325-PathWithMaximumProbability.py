# Last updated: 7/12/2025, 11:52:35 PM
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)

        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        
        pq = [(-1.0, start)]  # Start with a probability of 1, stored as -1 for max-heap
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return -prob  # Convert back to positive before returning
            for nei, edgeprob in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeprob, nei))
        
        return 0.0