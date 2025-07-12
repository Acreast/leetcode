// Last updated: 7/12/2025, 11:43:34 PM
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int finalXOR = 0;

        for (int num : nums){
            finalXOR = finalXOR ^ num;
        }

        int count = 0;
        while (k || finalXOR) {

            if ((k%2) != (finalXOR % 2)){
                count += 1;
            }

            k /= 2;
            finalXOR /= 2;
        }

        return count;
    }
};