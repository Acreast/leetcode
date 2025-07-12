# Last updated: 7/12/2025, 11:55:25 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(node):
            if not node:
                return
            for c in node.children:
                traverse(c)
            res.append(node.val)
        traverse(root)
        return res