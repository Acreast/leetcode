# Last updated: 7/12/2025, 11:52:45 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def construct_bst(values):
            if not values:
                return None
            mid = len(values)//2
            root = TreeNode(values[mid])
            root.left = construct_bst(values[:mid])
            root.right = construct_bst(values[mid + 1:])
            return root
        
        sorted_values = inorder(root)
        return construct_bst(sorted_values)
