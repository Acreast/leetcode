# Last updated: 7/12/2025, 11:47:29 PM
from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)
        visit = [False] * N
        longest_cycle = 0
        length_2_cycles = []

        # Detect cycles and their lengths
        for i in range(N):
            if visit[i]:
                continue
            
            cur = i
            stack = []
            index_map = {}

            while cur not in index_map and not visit[cur]:
                visit[cur] = True
                index_map[cur] = len(stack)
                stack.append(cur)
                cur = favorite[cur]
            
            if cur in index_map:
                # Found a cycle
                cycle_start = index_map[cur]
                cycle_length = len(stack) - cycle_start
                longest_cycle = max(longest_cycle, cycle_length)

                if cycle_length == 2:
                    length_2_cycles.append(stack[cycle_start:])
        
        # Build inverted graph for chains
        inverted = defaultdict(list)
        for src, dst in enumerate(favorite):
            inverted[dst].append(src)
        
        def bfs(src, exclude):
            """Find the longest chain starting from src, excluding a specific node."""
            q = deque([(src, 0)])
            max_length = 0

            while q:
                node, length = q.popleft()
                max_length = max(max_length, length)

                for neighbor in inverted[node]:
                    if neighbor != exclude:
                        q.append((neighbor, length + 1))
            
            return max_length

        # Process length-2 cycles and their chains
        chain_sum = 0
        for n1, n2 in length_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain_sum, longest_cycle)
