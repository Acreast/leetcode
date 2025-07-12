// Last updated: 7/12/2025, 11:50:59 PM
#include <vector>
#include <unordered_map>
#include <queue>

class Solution {
public:
    int findLeastNumOfUniqueInts(std::vector<int>& arr, int k) {
        std::unordered_map<int, int> freq;
        for (int num : arr) {
            freq[num]++;
        }

        std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
        for (const auto& entry : freq) {
            minHeap.push(entry.second);
        }

        int res = minHeap.size();
        while (k > 0 && !minHeap.empty()) {
            int f = minHeap.top();
            minHeap.pop();

            if (k >= f) {
                k -= f;
                res--;
            }
        }

        return res;
    }
};
