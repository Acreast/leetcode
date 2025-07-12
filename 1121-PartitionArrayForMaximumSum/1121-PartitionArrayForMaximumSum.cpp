// Last updated: 7/12/2025, 11:53:24 PM
#include <vector>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    int maxSumAfterPartitioning(std::vector<int>& arr, int k) {
        std::unordered_map<int, int> cache;

        // Define the inner function as a lambda
        std::function<int(int)> dfs = [&](int i) -> int {
            if (cache.count(i)) {
                return cache[i];
            }

            int result = 0;
            int curr_max = 0;
            for (int j = i; j < std::min(static_cast<int>(arr.size()), k + i); ++j) {
                curr_max = std::max(arr[j], curr_max);
                int window_size = j - i + 1;
                result = std::max(result, dfs(j + 1) + curr_max * window_size);
            }

            cache[i] = result;
            return result;
        };

        return dfs(0);
    }
};