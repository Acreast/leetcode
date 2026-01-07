# Last updated: 1/8/2026, 12:15:28 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        MOD = 10 ** 9 + 7
10        def dfs(node):
11            if not node:
12                return 0
13            
14            node.val += dfs(node.left) + dfs(node.right)
15            return node.val
16        
17        total = dfs(root)
18
19        res = 0
20        queue = deque([root])
21
22        while queue:
23            node = queue.popleft()
24            if not node:
25                continue
26            node_total = ((total - node.val) * node.val )
27            res = max(res, node_total)
28
29            if node.left:
30                queue.append(node.left)
31            if node.right:
32                queue.append(node.right)
33
34        return res  % MOD