// Last updated: 7/12/2025, 11:54:17 PM
class Solution {
public:
    int sumSubarrayMins(std::vector<int>& arr) {
        const int MOD = 1000000007;
        int res = 0;
        std::stack<std::pair<int, int>> stack;  // index, num

        for (int i = 0; i < arr.size(); ++i) {
            while (!stack.empty() && arr[i] < stack.top().second) {
                auto [j, m] = stack.top();
                stack.pop();
                int left = j - (stack.empty() ? -1 : stack.top().first);
                int right = i - j;
                res = (res + static_cast<long long>(m) * left * right) % MOD;
            }
            stack.push({i, arr[i]});
        }

        while (!stack.empty()) {
            auto [j, n] = stack.top();
            stack.pop();
            int left = j - (stack.empty() ? -1 : stack.top().first);
            int right = arr.size() - j;
            res = (res + static_cast<long long>(n) * left * right) % MOD;
        }

        return res;
    }
};