// Last updated: 7/12/2025, 11:53:50 PM
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int l = 0;
        int r = nums.size() -1;
        deque<int> deque;
        while (l <= r) {
            if (nums[r] * nums[r] > nums[l] * nums[l]){
                deque.push_front(nums[r] * nums[r]);
                r -= 1;
            } else {
                deque.push_front(nums[l] * nums[l]);
                l += 1;
            }
        }
        vector<int> res;
        while(!deque.empty()) {
            res.push_back(deque.front());
            deque.pop_front();
        }
        return res;
    }
};