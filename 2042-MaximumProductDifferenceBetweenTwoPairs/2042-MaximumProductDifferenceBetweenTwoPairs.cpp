// Last updated: 7/12/2025, 11:48:39 PM
class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        // sort(nums.begin(), nums.end());
        // int size = nums.size();
        // return abs(nums[0] * nums[1] - nums[size -1] * nums[size -2]);
        int largest = 0, secondLargest = 0;
        int smallest = INT_MAX, secondSmallest = INT_MAX;

        for (int n : nums) {
            if (n < smallest) {
                secondSmallest = smallest;
                smallest = n;
            } else if (n < secondSmallest) {
                secondSmallest = n;
            }

            if (n > largest) {
                secondLargest = largest;
                largest = n;
            } else if (n > secondLargest) {
                secondLargest = n;
            }
        }

        return (largest * secondLargest) - (smallest * secondSmallest);
    }
};