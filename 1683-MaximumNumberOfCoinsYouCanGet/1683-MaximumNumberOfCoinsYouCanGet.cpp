// Last updated: 7/12/2025, 11:50:30 PM
class Solution {
public:
    int maxCoins(vector<int>& A) {
        sort(A.begin(), A.end());
        int res = 0, n = A.size();
        for (int i = n / 3; i < n; i += 2)
            res += A[i];
        return res;
    }
};