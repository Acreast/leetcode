// Last updated: 7/12/2025, 11:50:12 PM
class Solution {
public:
    int maxDepth(string s) {
        int res = 0;
        int counter = 0;
        for (char c: s) {
            if (c == '(') {
                counter +=1;
            }
            if (c == ')') {
                counter -=1;
            }
            res = max(res,counter);
        }
        return res;
    }
};