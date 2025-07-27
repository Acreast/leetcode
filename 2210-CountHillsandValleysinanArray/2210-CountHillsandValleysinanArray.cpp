// Last updated: 7/27/2025, 5:15:19 PM
class Solution {
public:
    int countHillValley(vector<int>& nums) {
        vector<int> cleaned;
        cleaned.push_back(nums[0]);

        for (int i = 1; i < nums.size(); ++i ) {
            if (nums[i] != cleaned.back()) {
                cleaned.push_back(nums[i]);
            }
        }

        int res = 0;

        for (int i = 1; i < cleaned.size() - 1; ++i) {
            if ( (cleaned[i] < cleaned[i - 1] && cleaned[i] < cleaned[i + 1]) || (cleaned[i] > cleaned[i - 1] && cleaned[i] > cleaned[i + 1])) {
                res += 1;
            }
        }

        return res;
    }
};