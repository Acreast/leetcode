// Last updated: 9/27/2026, 2:13:18 AM
1#include <string>
2#include <vector>
3#include <unordered_map>
4
5class Solution {
6public:
7    string evaluate(string s, vector<vector<string>>& knowledge) {
8        unordered_map<string, string> dict;
9        for (const auto& kv : knowledge) {
10            dict[kv[0]] = kv[1];
11        }
12
13        string result = "";
14        string key = "";
15        bool inside = false;
16
17        for (char c : s) {
18            if (c == '(') {
19                inside = true;
20                key = "";
21            } else if (c == ')') {
22                inside = false;
23                auto it = dict.find(key);
24                if (it != dict.end()) {
25                    result += it->second;
26                } else {
27                    result += "?";
28                }
29            } else {
30                if (inside) {
31                    key += c;
32                } else {
33                    result += c;
34                }
35            }
36        }
37
38        return result;
39    }
40};