// Last updated: 7/12/2025, 11:51:49 PM
class Solution {
public:
    int minSteps(string s, string t) {
        std::vector<int> count_s(26,0);
        std::vector<int> count_t(26,0);

        for (char c: s){
            count_s[c - 'a' ]++;
        }
        for (char c: t){
            count_t[c - 'a' ]++;
        }

        int steps = 0;
        for (int i = 0; i < 26; i++){
            steps += std::abs(count_s[i] - count_t[i]);
        }

        return steps/2;
    }
};