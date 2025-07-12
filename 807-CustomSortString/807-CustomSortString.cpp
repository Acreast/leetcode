// Last updated: 7/12/2025, 11:55:12 PM
class Solution {
public:
    string customSortString(string order, string s) {
        string result = "";
        unordered_map <int,int> mapping;
        for (auto &it : s) {
            mapping[it]++;
        }

        for (auto &it : order) {
            if (mapping.find(it) != mapping.end()){
                result.append(mapping[it], it);
                mapping.erase(it);
            }
        }
        for(auto &it: mapping) {
            result.append(it.second,it.first);
        }
        return result;
    }
};