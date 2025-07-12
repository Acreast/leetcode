// Last updated: 7/12/2025, 11:51:11 PM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pseudoPalindromicPaths(TreeNode* root) {
        unordered_map<int, int> count;
        int odd = 0;

        function<int(TreeNode*)> dfs = [&](TreeNode* curr) {
            if (!curr) {
                return 0;
            }

            count[curr->val]++;
            int oddChange = (count[curr->val] % 2 == 1) ? 1 : -1;
            odd += oddChange;

            int res;
            if (!curr->left && !curr->right) {
                res = (odd <= 1) ? 1 : 0;
            } else {
                res = dfs(curr->left) + dfs(curr->right);
            }

            odd -= oddChange;
            count[curr->val]--;
            return res;
        };

        return dfs(root);
    }
};
