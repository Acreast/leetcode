// Last updated: 2/9/2026, 1:16:36 AM
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
17
18    static int height(TreeNode node) {
19        if (node == null)
20            return 0;
21
22        // Height = 1 + max of left height and right heights
23        return 1 + Math.max(height(node.left), height(node.right));
24    }
25
26    // Function to check if the binary tree with given root
27    // is height-balanced
28    static boolean isBalanced(TreeNode root) {
29        if (root == null)
30            return true;
31
32        // Get the height of left and right sub trees
33        int lHeight = height(root.left);
34        int rHeight = height(root.right);
35
36        if (Math.abs(lHeight - rHeight) > 1)
37            return false;
38
39        // Recursively check the left and right subtrees
40        return isBalanced(root.left) && isBalanced(root.right);
41    }
42
43
44    // public boolean isBalanced(TreeNode root) {
45    //     // Function to calculate the height of a tree
46        
47
48    //     isbalanced(root);
49    // }
50}