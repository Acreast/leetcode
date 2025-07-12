// Last updated: 7/12/2025, 11:47:01 PM
class Solution {
public:
    string largestGoodInteger(string num) {
        string result = "";
        int res = -1;
        for(int i = 0; i + 2 < num.length(); i++) {
            if( !(num [i] == num[i+1] && num[i] == num[i + 2]) ) {
                continue;
            }
            res = std::max(res , num[i] - '0');
        }

        if ( res >= 0) {
            return std::string(3, '0' + res);
        }
        return "";
    
    }
};