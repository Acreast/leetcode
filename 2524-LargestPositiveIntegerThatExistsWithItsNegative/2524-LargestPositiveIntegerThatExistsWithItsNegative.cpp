// Last updated: 7/12/2025, 11:46:00 PM
class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int size = nums.size() -1;
        for (int i = size ; i >= 0 ; i--){
            if (nums[i] > 0 && binary_search(nums.begin(),nums.end(), -nums[i])) {
                return nums[i];
            }
        }
        return -1;
    }
};