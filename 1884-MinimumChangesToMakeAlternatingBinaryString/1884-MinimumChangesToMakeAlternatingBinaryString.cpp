// Last updated: 7/12/2025, 11:49:19 PM
class Solution {
public:
    int minOperations(string s) {
        char c_0 = s[0];
        int count1 = count(s, c_0);
        int count2 = count(s, c_0 == '0' ? '1' : '0') + 1;
        return min(count1, count2);
    }

private:
    int count(string s, char c_pre) {
        int count = 0;
        for (int i = 1; i < s.length(); i++) {
            char current = s[i];
            if (current == c_pre) {
                count++;
                c_pre = c_pre == '0' ? '1' : '0';
            } else {
                c_pre = current;
            }
        }
        return count;
    }
};
