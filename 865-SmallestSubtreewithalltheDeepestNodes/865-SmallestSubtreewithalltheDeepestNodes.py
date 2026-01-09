# Last updated: 1/10/2026, 12:50:48 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        def dfs(node):
10            if not node:
11                return 0, None
12            
13            left_depth, left_subtree = dfs(node.left)
14            right_depth, right_subtree = dfs(node.right)
15
16            if left_depth == right_depth:
17                return left_depth + 1, node
18            elif left_depth > right_depth:
19                return left_depth + 1, left_subtree
20            else:
21                return right_depth + 1, right_subtree
22
23
24        return dfs(root)[1]