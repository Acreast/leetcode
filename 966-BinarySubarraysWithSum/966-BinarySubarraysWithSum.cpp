// Last updated: 7/12/2025, 11:54:09 PM
#include <vector>
using namespace std;

class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        
        auto helper = [&](int goal) {
            if (goal < 0) {
                return 0;
            }

            int result = 0;
            int left = 0;
            int current = 0;
            for (int r = 0; r < nums.size(); r++) {
                current += nums[r];

                while (current > goal) {
                    current -= nums[left];
                    left += 1;
                }
                result += (r - left + 1); 
            }
            return result;
        };
        return (helper(goal) - helper(goal - 1));
    }
};