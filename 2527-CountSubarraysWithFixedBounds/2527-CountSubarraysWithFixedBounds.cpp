// Last updated: 7/12/2025, 11:46:07 PM
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long result = 0;
        int min_index = -1;
        int max_index = -1;
        int bad_index = -1;

        for (int i = 0; i < nums.size(); i ++) {
            if (!(minK <= nums[i] && nums[i] <= maxK)) {
                bad_index = i;
            }

            if(nums[i] == minK) {
                min_index = i;
            }

            if(nums[i] == maxK) {
                max_index = i;
            }

            result += max(0, min(min_index, max_index) - bad_index);
        }

        return result;

    }
};