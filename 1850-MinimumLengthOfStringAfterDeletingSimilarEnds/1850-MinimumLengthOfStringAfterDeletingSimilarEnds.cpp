// Last updated: 7/12/2025, 11:49:26 PM
class Solution {
public:
    int minimumLength(string s) {
        int l =0;
        int r = s.length() -1;
        while (l < r && s[l] == s[r]){
            char temp = s[l];
            while (l <= r && s[l] == temp) {
                l += 1;
            }
            while (r >= l && s[r] == temp) {
                r -= 1;
            }
        }
        return (r - l + 1);
    }
};