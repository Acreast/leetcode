// Last updated: 7/12/2025, 11:53:58 PM
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int score = 0;
        int res = 0;
        int l = 0;
        int r = tokens.size() - 1;
        
        while (l <= r) {
            if (power >= tokens[l]) {
                power -= tokens[l];
                l += 1;
                score += 1;
                res = max(res, score);
            } else if (score > 0) {
                power += tokens[r];
                r -= 1;
                score -= 1;
            } else {
                break;
            }
        }
        
        return res;
    }
};