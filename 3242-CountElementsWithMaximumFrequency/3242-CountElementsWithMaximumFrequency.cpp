// Last updated: 7/12/2025, 11:43:36 PM
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map <int,int> counter;
        int max = 0;
        int res = 0;
        for (int num : nums) {
            counter[num] += 1;
            max = std::max(counter[num],max);
        }

        for (auto item: counter){
            if (item.second == max){
                res += item.second;
            }
        }

        return res;



    }
};