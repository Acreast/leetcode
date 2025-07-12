// Last updated: 7/12/2025, 11:48:59 PM
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& A) {
        sort(A.begin(), A.end());
        int pre = 0;
        for (int& a : A)
            pre = min(pre + 1, a);
        return pre;
    }
};