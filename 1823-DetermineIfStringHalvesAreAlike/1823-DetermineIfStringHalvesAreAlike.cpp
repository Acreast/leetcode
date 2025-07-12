// Last updated: 7/12/2025, 11:49:32 PM
class Solution {
public:
    bool halvesAreAlike(string s) {
        auto countVowels = [](const string& str) {
            unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
           int count = 0;
           for (char c:str) {
               if(vowels.count(c) > 0) {
                   count ++;
               }
           } 
           return count;
        };

        int lengths = s.length();
        int midPoint = lengths /2;

        string firsthalf = s.substr(0, midPoint);
        string secondhalf = s.substr(midPoint);

        return countVowels(firsthalf) == countVowels(secondhalf);
    }
};