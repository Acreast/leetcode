// Last updated: 7/12/2025, 11:43:32 PM
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long result = -1;
        long long total = 0;

        for (int n : nums){
            if (total > n) {
                result = total + n;
               
            }
            total += n;
        }
        return result;
    }
};