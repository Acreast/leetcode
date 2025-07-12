// Last updated: 7/12/2025, 11:47:18 PM
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> positive_arr;
        vector<int> negative_arr;
        vector<int> res;
        for (int num: nums) {
            if (num > 0) {
                positive_arr.push_back(num);
            } else {
                negative_arr.push_back(num);
            }
        }

        for (int i = 0; i < nums.size()/2; i ++) {
            res.push_back(positive_arr[i]);
            res.push_back(negative_arr[i]);
        }

        return res;
    }
};