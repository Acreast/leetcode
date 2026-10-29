# Last updated: 10/30/2026, 12:21:13 AM
1class Tree:  # Euler tour: the subtree of x is tin[x] .. tout[x] - 1; LCA by a sparse table over the DFS order
2    def __init__(self, n: int, edges: list[list[int]]):
3        graph = [[] for _ in range(n)]
4        for u, v in edges:
5            graph[u].append(v)
6            graph[v].append(u)
7
8        parent, tin, tout, order = [0] * n, [0] * n, [0] * n, []  # the root is its own parent; order: the nodes in DFS order
9        stack = [0]
10        while stack:  # DFS without recursion; ~x marks the moment x's subtree is done
11            x = stack.pop()
12            if x < 0:
13                tout[~x] = len(order)
14                continue
15            tin[x] = len(order)
16            order.append(x)
17            stack.append(~x)
18            for y in graph[x]:
19                if y != parent[x]:
20                    parent[y] = x
21                    stack.append(y)
22
23        first = [[tin[parent[x]] for x in order]]  # first[k][i]: the earliest parent among order[i : i + 2^k]
24        for k in range(1, n.bit_length()):
25            prev = first[-1]
26            first.append([*map(min, prev, prev[1 << k - 1:])])
27        self.parent, self.tin, self.tout, self.order, self.first = parent, tin, tout, order, first
28
29    def lca(self, u: int, v: int) -> int:  # the parent that comes first in DFS order among the nodes after u up to v
30        if u == v:
31            return u
32        l, r = sorted((self.tin[u], self.tin[v]))
33        k = (r - l).bit_length() - 1
34        return self.order[min(self.first[k][l + 1], self.first[k][r - (1 << k) + 1])]
35
36
37class RootPaths:  # paths[x]: XOR of the letter bits from the root down to x
38    def __init__(self, tree: Tree, bit: list[int]):
39        self.start = start = bit[:]  # the masks for the initial letters: a parent comes before its children in DFS order
40        for x in tree.order[1:]:
41            start[x] ^= start[tree.parent[x]]
42        self.tin, self.tout = tree.tin, tree.tout
43        self.fenwick = [0] * (len(bit) + 1)  # a Fenwick tree over the Euler tour with the changes since the start
44
45    def flip(self, x: int, d: int):  # XOR d into the root path of every node in x's subtree
46        fenwick = self.fenwick
47        for i in self.tin[x] + 1, self.tout[x] + 1:  # d starts at x's subtree and cancels out after it
48            while i < len(fenwick):
49                fenwick[i] ^= d
50                i += i & -i
51
52    def __getitem__(self, x: int) -> int:
53        fenwick, mask, i = self.fenwick, self.start[x], self.tin[x] + 1
54        while i:
55            mask ^= fenwick[i]
56            i -= i & -i
57        return mask
58
59
60class Solution:
61    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
62        tree = Tree(n, edges)
63        bit = [1 << ord(c) - 97 for c in s]  # bit[x]: the bit of x's letter
64        paths = RootPaths(tree, bit)
65
66        ans = []
67        for q in queries:
68            kind, a, b = q.split()
69            if kind == 'update':
70                x, new_bit = int(a), 1 << ord(b) - 97
71                paths.flip(x, bit[x] ^ new_bit)  # the new letter changes the root path of every node in x's subtree
72                bit[x] = new_bit
73            else:
74                u, v = int(a), int(b)
75                mask = paths[u] ^ paths[v] ^ bit[tree.lca(u, v)]  # the LCA cancels out in paths[u] ^ paths[v], so add it back
76                ans.append(mask.bit_count() <= 1)  # at most one letter is odd
77        return ans