# Last updated: 11/22/2026, 1:04:38 AM
1class Solution:
2    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
3        children = [[] for _ in s]
4        for x in range(1, len(s)):
5            children[parent[x]].append(x)
6        size, last = [1] * len(s), {}  # last[c]: the deepest node with letter c on the path from the root
7
8        def dfs(x: int) -> None:
9            c = s[x]
10            above = last.get(c, -1)  # the closest ancestor with the same letter, or -1
11            last[c] = x
12            for child in children[x]:
13                dfs(child)
14            last[c] = above
15            if x:  # the root has no parent
16                size[above if above >= 0 else parent[x]] += size[x]
17
18        dfs(0)
19        return size