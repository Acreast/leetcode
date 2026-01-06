# Last updated: 1/6/2026, 9:01:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11
12        max_sum = float('-inf')
13        queue = deque([root])
14
15        level_index = 1
16        while queue:
17            level_size = len(queue)
18            level_sum = 0
19
20            for _ in range(level_size):
21                node = queue.popleft()
22                level_sum += node.val
23
24                if node.left:
25                    queue.append(node.left)
26                if node.right:
27                    queue.append(node.right)
28
29            if level_sum > max_sum:
30                res = level_index
31                max_sum = level_sum
32            level_index += 1
33
34        return res
35        
36
37
38        