# Last updated: 7/12/2025, 11:53:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur): 
            if not cur:
                return [0,0]

            leftSize, leftCoin = dfs(cur.left)
            rightSize, rightCoin = dfs(cur.right)

            size = (1 + leftSize + rightSize)
            coin = (cur.val + leftCoin + rightCoin)
            self.res += abs(size - coin)
            return [size, coin]
        
        dfs(root)
        
        return self.res