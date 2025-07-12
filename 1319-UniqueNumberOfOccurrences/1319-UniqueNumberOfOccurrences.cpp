// Last updated: 7/12/2025, 11:52:37 PM
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        vector<int> arr_count;
        int curr, prev;
        int count = 1;
        for (int i = 0; i < arr.size(); i ++) {
            if (i != arr.size() - 1 && arr[i + 1] == arr[i]) {
                count++;
            } else {
                arr_count.push_back(count);
                count = 1;
            }
        }

        sort(arr_count.begin(),arr_count.end());

        for (int i = 0; i < arr_count.size(); i ++) {
            if (i == arr_count.size() -1) {
                break;
            }
            if (arr_count[i+1] == arr_count[i]) {
                return false;
            }
        }

        return true;

    }
};