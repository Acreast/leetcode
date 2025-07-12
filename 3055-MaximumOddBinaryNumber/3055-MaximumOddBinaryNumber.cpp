// Last updated: 7/12/2025, 11:44:09 PM
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int size = s.length();
        int count_of_ones = 0;
        for (char c: s) {
            if (c == '1') {
                count_of_ones += 1;
            }
        }
        string result;
        for (int i = 0; i < s.length(); i ++){
            if (count_of_ones > 1) {
                result += "1";
                count_of_ones -=1;
                continue;
            } else if (i == s.length() -1){
                result += "1";
                return result;
            }
            result += "0";
        }
        return result;   
    }
};