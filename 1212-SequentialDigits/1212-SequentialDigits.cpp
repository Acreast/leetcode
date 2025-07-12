// Last updated: 7/12/2025, 11:53:06 PM
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> sequentialDigits(int low, int high) {
        std::vector<int> result;
        
        for (int i = 1; i <= 9; ++i) {
            int num = i;
            int next = i;

            while (num <= high && next <= 9) {
                if (num >= low) {
                    result.push_back(num);
                }

                next++;
                num = num * 10 + next;
            }
        }

        std::sort(result.begin(), result.end()); // Ensure the result is sorted
        return result;
    }
};
