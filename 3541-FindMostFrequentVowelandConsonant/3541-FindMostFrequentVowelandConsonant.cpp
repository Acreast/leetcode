// Last updated: 9/13/2025, 9:21:50 PM
class Solution {
public:
    int maxFreqSum(string s) {
        int freq[26], max_vowel = 0, max_conso = 0;

        for (char c: s) {
            int i = c - 'a';
            freq[i] ++;

            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                max_vowel = max(freq[i], max_vowel);
            } else {
                max_conso = max(freq[i], max_conso);
            }
        }

        return max_vowel + max_conso;
    }
};