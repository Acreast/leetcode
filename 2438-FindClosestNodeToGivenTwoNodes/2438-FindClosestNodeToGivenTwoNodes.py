# Last updated: 7/12/2025, 11:46:38 PM
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def bfs(src, dist_map):
            q = deque()
            q.append([src,0])
            dist_map[src] = 0
            while q:
                node, dist = q.popleft()
                for nei in adj_list[node]:
                    if nei not in dist_map:
                        q.append([nei,dist + 1])
                        dist_map[nei] = dist + 1

        adj_list = defaultdict(list)
        for i, dst in enumerate(edges):
            adj_list[i].append(dst)
        
        dist_map1 = {}
        dist_map2 = {}
        bfs(node1, dist_map1)
        bfs(node2, dist_map2)

        res = -1
        result_dist = float("inf")

        for i in range(len(edges)):
            if i in dist_map1 and i in dist_map2:
                dist = max(dist_map1[i], dist_map2[i])
                if dist < result_dist:
                    result_dist = dist
                    res = i
        return res
