// Last updated: 7/12/2025, 11:49:47 PM
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1 = "";
        string s2 = "";


        std::string word1_concatenanted = "";
        std::string word2_concatenanted = "";

        for(const string& s: word1) {
            word1_concatenanted += s;
        }
        for(const string& s: word2) {
            word2_concatenanted += s;
        }

        return word1_concatenanted == word2_concatenanted;
    }
};