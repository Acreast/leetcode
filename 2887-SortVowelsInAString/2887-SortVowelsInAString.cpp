// Last updated: 7/12/2025, 11:44:22 PM
class Solution {
public:
    string sortVowels(string s) {
        std::vector<char> vowels;

        // Iterate over each character in the string
        for (char c : s) {
            // Check if the lowercase version of the character is a vowel
             if (string("aeiouAEIOU").find(c) != string::npos) {
                vowels.push_back(c);
            }
        }

        // Sort the vector of vowels in reverse order
        std::sort(vowels.rbegin(), vowels.rend());
        string res;
        for(char c : s) {
            if (string("aeiouAEIOU").find(c) != string::npos) {
                res += vowels.back();
                vowels.pop_back();
            } else {
                res += c;
            }
        }

        return res;
    }
};