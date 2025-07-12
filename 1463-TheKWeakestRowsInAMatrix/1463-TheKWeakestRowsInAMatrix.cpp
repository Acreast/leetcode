// Last updated: 7/12/2025, 11:51:52 PM
class Solution {
#include <map>
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
    int n = mat[0].size();
    for (int i = 0; i<mat.size(); i++) {
        mat[i].push_back(i);
    }
    sort(mat.begin(), mat.end());
    vector<int> ans(k);
    for (int i = 0; i <k ; i++) {
        ans [i] =mat[i][n];
    }
    return ans;
    }
};