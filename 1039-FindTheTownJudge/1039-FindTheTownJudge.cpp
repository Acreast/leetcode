// Last updated: 7/12/2025, 11:53:42 PM
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        unordered_map<int,int> incomingtrust;
        unordered_map<int,int> outgoingtrust;
        for (auto single_trust: trust) {
            incomingtrust[single_trust[1]] += 1;
            outgoingtrust[single_trust[0]] += 1;
        }
        for (int i = 1; i <=n; i ++) {
            if (incomingtrust[i] == n-1 && outgoingtrust[i] == 0) {
                return i;
            }
        }
        return -1;
    }
};