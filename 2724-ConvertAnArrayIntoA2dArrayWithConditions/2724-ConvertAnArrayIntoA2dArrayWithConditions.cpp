// Last updated: 7/12/2025, 11:44:53 PM
class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        std::unordered_map<int,int> count;
        vector<vector<int>> res;

        for (int n : nums){
            int row = count[n];
            if (res.size() == row) {
                res.push_back({});
            }
            res[row].push_back(n);
            count[n] += 1;
        }

        return res;
    }
};