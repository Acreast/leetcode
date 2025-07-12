// Last updated: 7/12/2025, 11:54:29 PM
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        sort(people.begin(),people.end());
        int l = 0;
        int r = people.size() -1;
        int result = 0;
        while (l <= r) {
            if (l == r) {
                result += 1;
                break;
            }
            int remain = limit - people[r];
            if (l <= r && people[l] <= remain) {
                result +=1;
                l += 1;
                r -= 1;
            } else {
                result += 1;
                r -= 1;
            }
        }
        return result;
    }
};