# Last updated: 7/12/2025, 11:45:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def count_swaps(cur_level):
            swaps = 0
            index_map = {n:i for i,n in enumerate(cur_level)}
            sorted_arr = sorted(cur_level)

            for i in range(len(cur_level)):
                if cur_level[i] != sorted_arr[i]:

                    swaps += 1
                    j = index_map[sorted_arr[i]]
                    cur_level[i], cur_level[j] = cur_level[j], cur_level[i] 
                    index_map[cur_level[i]] = i
                    index_map[cur_level[j]] = j
            return swaps

        q = deque([root])
        res = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res += count_swaps(level)
        
        return res