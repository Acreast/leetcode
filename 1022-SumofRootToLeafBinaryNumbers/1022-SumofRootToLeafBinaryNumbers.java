// Last updated: 2/25/2026, 8:53:57 PM
1/**
2 * Definition for a binary tree node.
3 * public class TreeNode {
4 *     int val;
5 *     TreeNode left;
6 *     TreeNode right;
7 *     TreeNode() {}
8 *     TreeNode(int val) { this.val = val; }
9 *     TreeNode(int val, TreeNode left, TreeNode right) {
10 *         this.val = val;
11 *         this.left = left;
12 *         this.right = right;
13 *     }
14 * }
15 */
16class Solution {
17    public int sumRootToLeaf(TreeNode root) {
18        return dfs(root, 0);
19    }
20
21
22    private static int dfs(TreeNode node, int curr) {
23        if (node == null) return 0;
24
25        curr = curr * 2 + node.val;
26
27        if (node.left == null && node.right == null) {
28            return curr;
29        }
30
31        return dfs(node.left, curr) + dfs(node.right, curr);
32    }
33}