// Last updated: 7/12/2025, 11:48:37 PM
class Solution {
public:
    long long wonderfulSubstrings(string word) {
        vector <long long> count (1024,0);
        long long result = 0;
        int prefixXor = 0;
        count[prefixXor] = 1;

        for (char c: word) {
            int charIndex = c - 'a';
            prefixXor ^= 1 << charIndex;
            result += count[prefixXor];
            for (int i = 0; i < 10; i++) {
                result += count[prefixXor ^ (1 << i)];
            }
            count[prefixXor] ++;

        }

        return result;
    }
};