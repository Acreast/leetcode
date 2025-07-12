// Last updated: 7/12/2025, 11:43:42 PM
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int l = 0;
        int r = 0;
        int result = 0;
        unordered_map <int,int> counter;
        for (int r = 0; r < nums.size(); r ++) {
            counter[nums[r]] += 1;
            while(counter[nums[r]] > k) {
                counter[nums[l]] -= 1;
                l += 1;
            }
            result = std::max(result, (r - l + 1));
        }
        return result;
    }
};