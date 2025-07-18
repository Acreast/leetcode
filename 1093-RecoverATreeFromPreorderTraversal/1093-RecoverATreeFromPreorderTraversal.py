# Last updated: 7/12/2025, 11:53:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.s = traversal
        self.idx = 0
        self.level = 0
        node = TreeNode(-1)
        self.helper(node, 0)
        return node.left

    def helper(self, parent, lvl):
        while self.idx < len(self.s) and lvl == self.level:
            num = 0
            while self.idx < len(self.s) and self.s[self.idx].isdigit():
                num = num * 10 + int(self.s[self.idx])
                self.idx += 1
            node = TreeNode(num)
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            self.level = 0
            while self.idx < len(self.s) and self.s[self.idx] == '-':
                self.level += 1
                self.idx += 1
            self.helper(node, lvl + 1)
        