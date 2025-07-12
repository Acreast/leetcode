// Last updated: 7/12/2025, 11:49:42 PM
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        unordered_map <int,int> counter;

        for (auto type: students) {
            counter[type] += 1;
        }

        int remaining = sandwiches.size();
        for (int sandwich:sandwiches){
            if (counter[sandwich] == 0){
                break;
            }
            if (remaining == 0) {
                break;
            }
            counter[sandwich]--;
            remaining--;
        }
        return remaining;


    }
};