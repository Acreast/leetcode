// Last updated: 7/12/2025, 11:50:03 PM
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        std::unordered_map<char, int> char_index;
        int res = -1;

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (char_index.find(c) != char_index.end()) {
                res = std::max(res, i - char_index[c] - 1);
            } else {
                char_index[c] = i;
            }
        }

        return res;
    }
};