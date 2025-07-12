// Last updated: 7/12/2025, 11:51:01 PM
class Solution {
public:
    double average(vector<int>& s) {
         return (accumulate(begin(s), end(s), 0.) - *min_element(begin(s), end(s)) 
        - *max_element(begin(s), end(s))) / (s.size() - 2);
    }
};