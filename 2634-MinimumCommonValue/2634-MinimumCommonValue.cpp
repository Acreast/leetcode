// Last updated: 7/12/2025, 11:45:26 PM
class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int p1 = 0;
        int p2 = 0;
        while (true) {
            if (p1> nums1.size() -1 || p2 > nums2.size() -1) {
                return -1;
            }
            if (nums1[p1] == nums2[p2]) {
                return nums1[p1];
            }
            if (nums1[p1]> nums2[p2]) {
                p2 += 1;
            } else if (nums1[p1] < nums2[p2]) {
                p1 += 1;
            }
        }
        return 0;
    }
};

auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();