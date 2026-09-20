// Last updated: 9/21/2026, 2:07:32 AM
1class Solution {
2public:
3    int reverseDegree(string s) {
4        int res = 0;
5
6        for (int i = 0; i < s.length() ; i ++) 
7        {
8            char c = s[i];
9            int reversed_index = (int)c - (int)'a' - 26;
10            int prod = reversed_index * (i + 1);
11            res += abs(prod);
12        }
13
14        return res;
15    }
16};