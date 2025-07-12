// Last updated: 7/12/2025, 11:49:49 PM
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        std::vector<int> freq1(26,0);
        std::vector<int> freq2(26,0);

        for (char c: word1) {
            freq1[ c - 'a' ]++;
        }
        for (char c: word2) {
            freq2[ c - 'a' ]++;
        }

        for (int i = 0; i < 26; i++) {
            if((freq1[i] == 0 && freq2[i] != 0) || (freq1[i] != 0 && freq2[i] == 0)) {
                return false;
            }
        }

        std::sort(freq1.begin(),freq1.end());
        std::sort(freq2.begin(),freq2.end());

        for (int i = 0; i < 26; i++){
            if (freq1[i] != freq2[i]) {
                return false;
            }
        }

        return true;
    }
};