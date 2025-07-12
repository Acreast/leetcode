// Last updated: 7/12/2025, 11:47:47 PM
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        
        int res = 0;

        for (int i = 0; i < tickets.size(); i++) {

            if (i <= k) {
                res += std::min(tickets[i], tickets[k]);
            } else {
                res += std::min(tickets[i], tickets[k]-1);
            }
        }
        return res;
    }
};