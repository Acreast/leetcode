// Last updated: 7/12/2025, 11:54:48 PM
class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int res = 0, last = -1, n = seats.size();
            for(int i = 0; i < n ; ++i){
                if(seats[i] == 1){
                    res = last < 0 ? i : max(res, (i - last)/2);
                    last = i;
                }
            }
        res = max(res, n - last - 1);
        return res;
            
    }
};