// Last updated: 7/23/2025, 9:46:02 PM
class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int result = 0;
        if (x > y) {
            result += removePairs(s, 'a', 'b', x);
            result += removePairs(s, 'b', 'a', y);
        } else {
            result += removePairs(s, 'b', 'a', y);
            result += removePairs(s, 'a', 'b', x);
        }

        return result;
    }
    int removePairs(std::string &s, char first, char second, int score) {
        std::string temp;
        int count = 0;

        for (char c: s) {
            if (!temp.empty() && temp.back() == first && c == second) {
                temp.pop_back();
                count += score;
            } else {
                temp.push_back(c);
            }

        }
        s = temp;
        return count;
    }
};

