# Last updated: 10/7/2025, 11:40:01 PM
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        res = [-1] * N
        future = defaultdict(deque)
        for i, lake in enumerate(rains):
            if lake > 0:
                future[lake].append(i)
        
        full = set()
        heap = []

        for i, lake in enumerate(rains):
            if lake in full:
                return []
            
            if lake > 0:
                full.add(lake)
                future[lake].popleft()
                if future[lake]:
                    heapq.heappush(heap, (future[lake][0], lake))
            else:
                if heap:
                    _ ,lake = heapq.heappop(heap)
                    full.remove(lake)
                    res[i] = lake
                else:
                    res[i] = 1
        return res

