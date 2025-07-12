// Last updated: 7/12/2025, 11:47:30 PM
class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int prev = 0;
        int res = 0;
        for( string s : bank) {
            int count = 0;
            for (char c : s) {
                if (c == '1') {
                    count += 1;
                }
            }
            res += (count * prev);
            if ( count > 0 ) {
                prev = count;
            }
        }
        return res;
    }
};