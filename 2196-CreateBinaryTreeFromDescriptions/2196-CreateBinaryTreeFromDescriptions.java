// Last updated: 6/7/2026, 10:53:18 PM
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
17    public TreeNode createBinaryTree(int[][] descriptions) {
18        HashMap<Integer, TreeNode> nodes = new HashMap<>();
19        HashSet<Integer> children = new HashSet<>();
20
21        for (int i = 0; i < descriptions.length; i ++) {
22            int[] desc = descriptions[i];
23            int parent = desc[0]; 
24            int child = desc[1]; 
25            int isLeft = desc[2];
26
27            children.add(child);
28            if (!nodes.containsKey(parent))
29                nodes.put(parent,new TreeNode(parent));
30            
31            if (!nodes.containsKey(child))
32                nodes.put(child,new TreeNode(child));
33            
34            if (isLeft == 1) {
35                TreeNode curNode = nodes.get(parent);
36                curNode.left = nodes.get(child);
37            } else {
38                TreeNode curNode = nodes.get(parent);
39                curNode.right = nodes.get(child);
40            }
41        }
42
43        for (int i = 0; i < descriptions.length; i ++) {
44            int[] desc = descriptions[i];
45            int parent = desc[0]; 
46            if (!children.contains(parent)) {
47                return nodes.get(parent);
48            }
49        }
50
51        return new TreeNode(0);
52    }
53}