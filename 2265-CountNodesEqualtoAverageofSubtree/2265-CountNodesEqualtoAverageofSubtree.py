# Last updated: 9/11/2026, 12:36:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        res = 0
10        def dfs(node):
11            nonlocal res
12            if not node:
13                return [0,0]
14            leftTree = dfs(node.left)
15            rightTree = dfs(node.right)
16
17            sum = leftTree[0] + rightTree[0]  + node.val
18            nodeNum = leftTree[1] + rightTree[1] + 1
19
20            if sum // nodeNum == node.val:
21                res += 1
22            
23            return [sum, nodeNum]
24        
25        dfs(root)
26        return res
27
28        
29
30
31
32
33
34
35
36
37