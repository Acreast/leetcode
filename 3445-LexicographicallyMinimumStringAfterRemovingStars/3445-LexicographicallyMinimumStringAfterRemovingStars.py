# Last updated: 7/12/2025, 11:43:04 PM
class Solution:
    def clearStars(self, s: str) -> str:
        hash_map = defaultdict(deque)
        min_heap = []
        N = len(s)
        keep = [True] * N

        for i in range(N):
            if s[i] == "*":
                smallest = heapq.heappop(min_heap)
                index = hash_map[smallest].pop()
                keep[i] = False
                keep[index] = False
            else:
                heapq.heappush(min_heap, s[i])
                hash_map[s[i]].append(i)

        return ''.join(s[i] for i in range(N) if keep[i])